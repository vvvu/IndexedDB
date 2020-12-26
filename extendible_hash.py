class extendible_hash:
    class Bucket:

        def __init__(self, local_depth=1):
            self.mp = {}  # {key, value}
            self.local_depth = local_depth

        def get(self, key):
            return self.mp[key]

        def insert(self, key, value):
            self.mp[key] = value

        def remove(self, key):
            try:
                del self.mp[key]
            except KeyError:
                pass

    def __init__(self):
        self.global_depth = 1
        self.bucket_size = 50  # bucket_max_size
        '''
        [Very Important]
        Bucket_max_size will affect the efficiency of extendible
        because it will directly affect the frequency of split
        According to some related paper, we choose to assign 50 to bucket_size
        and finally get good performance
        '''
        self.size = 0
        num_buckets = pow(2, self.global_depth)
        self.dictionaries = [self.Bucket() for i in range(num_buckets)]

    def dst_bucket(self, key):  # destination bucket
        LSB = lambda i, n: i & ((1 << n) - 1)
        bucket_id = LSB(hash(key), self.global_depth)
        bkt = self.dictionaries[bucket_id]
        return bkt

    def get(self, key):
        bucket = self.dst_bucket(key)
        return bucket.get(key)

    def insert(self, key, value):
        bucket = self.dst_bucket(key)
        if key not in bucket.mp:
            self.size += 1
        bucket.insert(key, value)

        if len(bucket.mp) > self.bucket_size:  # split or rehashing
            self.split(bucket)

    def remove(self, key):
        bucket = self.dst_bucket(key)
        bucket.remove(key)
        self.size -= 1

    def split(self, bucket):
        '''
        when bucket's local_depth < global_depth => split and allocate a new bucket
        - Both the new bucket are assigned local depth d + 1
        - The overflowed bucket contents are rehashed
        when bucket's local_depth == global_depth => split and rehashing
        - global_depth = global_depth * 2
        '''
        if bucket.local_depth == self.global_depth:
            self.dictionaries *= 2
            self.global_depth += 1

        # split into two new bucket x/y
        nbkt_x, nbkt_y = self.Bucket(), self.Bucket()
        nbkt_x.local_depth = nbkt_y.local_depth = bucket.local_depth + 1

        LSB = lambda i, n: i & ((1 << n) - 1)  # least significant bit
        LnTH_bit = lambda i, n: (i >> n) & 1 == 1
            # Determine whether the [Last nTH BIT] is 1 or 0 to mapped to nbky_x or nbky_y

        for key, value in bucket.mp.items():
            bkt_id = LSB(hash(key), self.global_depth)  # mapped to new bucket
            dst_bkt = nbkt_x if LnTH_bit(bkt_id, bucket.local_depth) else nbkt_y  # mapped to nbkt_x | nbkt_y
            dst_bkt.insert(key, value)

        for idx, bkt in enumerate(self.dictionaries):  # make other old bucket point to new bucket
            if bkt != bucket:
                continue
            self.dictionaries[idx] = nbkt_x if LnTH_bit(idx, bucket.local_depth) else nbkt_y
