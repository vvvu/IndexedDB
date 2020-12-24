def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def getattr_index(lst, interlist):
    __index__ = []
    for attr in interlist:
        __index__.append(lst.index(attr))
    return __index__


lsb = lambda num, n : num & ((1 << n) - 1) # Get n least significants bits from Integer num
