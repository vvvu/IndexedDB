import os
import time
from conditional_query import *
from utils import *
from extendible_hash import *
from linear_hash import *

class test_query():

    def __init__(self,table_name):
        '''
        :param test_table_name : table_name
        '''
        self.table_name=table_name
        self.TB = {}  # {table_name, table_name_list}
        self.PK = {}  # {table_name, primary_key}
        self.index_table = None  # index table
        self.index_available = False  # 是否可用index

    def search(self, attr, value, cond_func):
        '''
        :param attr: 属性
        :param value: 值
        :param cond_func: 条件查询对应的函数
        :return: 返回条件查询的结果，以list形式存储
        '''
        return cond_func(self, attr, value)

    def print(self, query_table, head=5, cols: list = None):  # 输出查询结果
        '''
        :param query_table: search()得到的查询结果，以list存储
        :param head: 返回查询结果的前head个元素，默认为5
        :param cols: list，传入想要进行列筛选的列名（属性名）
        :return:
        '''
        if len(query_table) == 0:
            print("No query result")
        else:
            if cols != None:  # 列筛选
                attr_list = query_table[0].__attrs__
                inter_list = intersection(attr_list, cols)
                index = getattr_index(attr_list, inter_list)
                for idx, row in enumerate(query_table):
                    lst = []
                    for i in index:
                        lst.append(row.__values__[i])
                    print(lst)
                    if idx > head:
                        break
            else:
                for index, row in enumerate(query_table):
                    print(row.__values__)
                    if index > head:
                        break

    def create_indexing(self, indexing_method=extendible_hash):# 建立extendible_hash、linearhash_hash、extendible_hash、索引
        self.index_table = indexing_method()
        for index, row in enumerate(self.TB[self.table_name]):
            pk = self.TB[self.table_name][index].__values__[0]  # primary key = id <=> first element
            self.index_table.insert(pk, row)  # <id, row>
        self.index_available = True

    def create_row(self, name, attr):  # 表名，attr是一个dict，对应{attr, value}
        # TB
        # print(TB.keys())
        if name not in self.TB.keys():
            self.TB[name] = []
        dic = {
            "__attrs__": [],  # 存储属性
            "__values__": [],  # 存储对应的值
            "__repr__": lambda self: str(self.__values__),
        }
        for key, value in attr.items():
            dic[key] = value

        cls = type(name, (object,), dic)  # class，这里就是指声明一个具体的student

        for key, value in attr.items():
            cls.__attrs__.append(key)
            cls.__values__.append(value)

        if name not in self.PK.keys():
            self.PK[name] = cls.__attrs__[0]  # 默认第一个元素为Primary Key
        self.TB[name].append(cls)


def test1():
    tb = test_query('student')

    attr = ['id', 'name', 'sex', 'major', 'age', 'birthday', 'contact', 'credit']  # student 的属性
    fp = 'student.txt'
    with open(fp, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip().split('\t')
            d = {attr[i]: line[i] for i in range(0, len(attr))}  # 字典：映射属性和属性值
            tb.create_row('student', d)  # 在student表中加入对应项

    query_result = tb.search('age', (15, 20), between_and)  # 查询年龄在(15,20) 的人
    tb.print(query_result, head=10)  # 输出结果表中前10项

    # print(PK) {Table : Primary Key}


def test2():  # 列筛选
    tb = test_query('student')

    attr = ['id', 'name', 'sex', 'major', 'age', 'birthday', 'contact', 'credit']  # student 的属性
    fp = 'student.txt'
    with open(fp, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip().split('\t')
            d = {attr[i]: line[i] for i in range(0, len(attr))}  # 字典：映射属性和属性值
            tb.create_row('student', d)  # 在student表中加入对应项

    query_result = tb.search('age', 15, geq)  # 查询 >= 15岁的人
    tb.print(query_result, head=10, cols=['id', 'name'])  # 输出结果表中前10项

def test_indexing(indexing_method=extendible_hash):
    tb = test_query('student')  # 指定查询student表

    attr = ['id', 'name', 'sex', 'major', 'age', 'birthday', 'contact', 'credit']  # student 的属性
    fp = 'student.txt'
    with open(fp, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip().split('\t')
            d = {attr[i]: line[i] for i in range(0, len(attr))}  # 字典：映射属性和属性值
            tb.create_row('student', d)  # 在student表中加入对应项

    tb.create_indexing(indexing_method)  # 针对student表建立索引

    search_result = tb.search('id', '3', indexing_search)
    normal_query_result = tb.search('id', '3', equal)

    # output
    tb.print(search_result)
    tb.print(normal_query_result)



###########################               ############################
###########################  大量数据插入，查询测试   ############################
NRECORDS = 10 ** 5

def test_large_data(nrecords=NRECORDS, indexing_method=extendible_hash):
    keys = ["k%d" % i for i in range(nrecords)]
    vals = ["v%d" % i for i in range(nrecords)]
    start = time.time()
    m = indexing_method()
    for i in range(nrecords):
        m.insert(keys[i], vals[i])
    for i in range(nrecords):
        v = m.get(keys[i])
        assert v == vals[i], "Expected value %s for key %s, got %s" % (vals[i], keys[i], v)
    end = time.time()
    print("Time taken for %s for %d enties: %f seconds" % (str(indexing_method), nrecords, end - start))



###########################               ############################
###########################   生成数据 & 时间对比  ############################

def test_load_data(indexing_method=extendible_hash):  # 生成数据 & 时间对比
    '''
    输入文件第一行：attr
    第二行至末尾行：row
    '''
    tb = test_query('gen_test')  # 指定查询gen_test表

    attr = []
    idx = 0
    fp = 'gen_data.txt'
    with open(fp, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if idx == 0:
                attr = line.strip().split('\t')
            else:
                line = line.strip().split('\t')
                d = {attr[i]: line[i] for i in range(0, len(attr))}  # 字典：映射属性和属性值
                tb.create_row('gen_test', d)  # 在gen_test表中加入对应项

            idx = idx + 1

        import time
        st = time.time()
        tb.create_indexing(indexing_method)  # 针对gen_test表建立索引
        ed = time.time()
        print("build %s index : %f"%(str(indexing_method),ed - st))

        st = time.time()
        indexing_result = tb.search('id', '599', indexing_search)
        ed = time.time()
        print("%s index : %f"%(str(indexing_method),ed - st))

        st = time.time()
        normal_query_result = tb.search('id', '599', equal)
        ed = time.time()
        print("normal query : ", ed - st)

        # output
        tb.print(indexing_result)
        tb.print(normal_query_result)
