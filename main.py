from test import *

if __name__ == '__main__':
    #test1()
    #test2()
    #test_indexing(indexing_method=extendible_hash) #测试不同的索引
    #test_indexing(indexing_method=LinearHashMap)  # 测试不同的索引
    test_large_data(nrecords=10 ** 4, indexing_method=LinearHashMap) #测试多条数据插入，查询
    #test_large_data(nrecords=10 ** 4, indexing_method=extendible_hash)  # 测试多条数据插入，查询
    #test_load_data(indexing_method=extendible_hash)
    test_load_data(indexing_method=LinearHashMap)