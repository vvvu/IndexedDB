import math
import xxhash

class HashMap:
    def __init__(self, size=32, load_factor=0.75, grow=True):
        self.table = [EntryList() for _ in range(size)]
        self.nentries = 0
        self.load_factor = load_factor
        self.grow = grow

    def insert(self, k, v):
        bkt_idx = self._get_bucket_idx(k, len(self.table))
        self.table[bkt_idx].append(k, v)
        self.nentries += 1
        if self.grow and self._comput_load_factor() > self.load_factor:
            self._grow()

    def get(self, k):
        bkt_idx = self._get_bucket_idx(k, len(self.table))
        for entry in self.table[bkt_idx]:
            if entry.key == k:
                return entry.value

    def _comput_load_factor(self):
        return self.nentries / (3 * len(self.table))

    def _get_bucket_idx(self, k, size):
        return xxhash.xxh64(k).intdigest() % size

    def _grow(self):
        # we double the table size and rehash all the entries
        newsize = len(self.table) * 2
        new_table = [EntryList() for _ in range(newsize)]
        for bucket in self.table:
            for e in bucket:
                bucket_idx = self._get_bucket_idx(e.key, newsize)
                new_table[bucket_idx].append(e.key, e.value)
        self.table = new_table


class LinearHashMap(HashMap):
    def __init__(self, size=32, load_factor=0.75):
        super().__init__(size, load_factor)
        self.i = int(math.log2(size))
        self.split_idx = 0

    def _grow(self):
        split_idx = self.split_idx
        self.split_idx += 1
        old_bucket = self.table[split_idx]
        new_bucket = EntryList()
        self.table.append(new_bucket)
        # if we have grown to the next power of 2 number of buckets
        # we increment i
        if len(self.table) > (1 << self.i):
            self.i += 1
        # if we have doubled the number of buckets, we reset s to 0
        if self.split_idx * 2 == len(self.table):
            self.split_idx = 0
        # rehash the entries in the old bucket and split with new bucket
        prev_e = old_bucket
        for e in old_bucket:
            new_bucket_id = self._get_bucket_idx(e.key, len(self.table))
            if new_bucket_id != split_idx:
                new_bucket.append(e.key, e.value)
                prev_e.next = e.next
            else:
                prev_e = e

    def _get_bucket_idx(self, k, size):
        h = xxhash.xxh64(k).intdigest()
        # we take the first i bits as the bucket index
        # if this index is less than the number of buckets
        # we return it as it is. Otherwise we unset the MSB
        # so we only use i-1 bits effectively and address the valid bucket
        bkt_idx = h & ((1 << self.i) - 1)
        if bkt_idx < size:
            return bkt_idx
        return bkt_idx ^ (1 << (self.i - 1))


class EntryList:
    def __init__(self):
        self.head = None

    def append(self, k, v):
        if self.head is None:
            self.head = Entry(k, v)
            return
        self.head.append(k, v)

    def __iter__(self):
        next = self.head
        while next:
            yield next
            next = next.next


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def append(self, k, v):
        new_entry = Entry(k, v)
        new_entry.next = self.next
        self.next = new_entry

