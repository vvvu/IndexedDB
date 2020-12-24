from conditional_query import *
from utils import *
from test import *
from extendible_hash import *


class query():

    def __init__(self, table_name):
        '''
        :param table_name: 待查询的表名
        '''
        self.table = TB[table_name]
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

    def indexing_linear_hash(self):
        pass
        # self.index_table = LinearHash()
        # for index, row in enumerate(self.table):
        #     pk = self.table[index].__values__[0] # primary key = id <=> first element
        #     self.index_table.insert(pk, row.__values__) # <id,row>
        # self.index_available = True

    def indexing_extendible_hash(self):  # 建立extendible_hash索引
        self.index_table = extendible_hash()
        for index, row in enumerate(self.table):
            pk = self.table[index].__values__[0]  # primary key = id <=> first element
            self.index_table.insert(pk, row)  # <id, row>
        self.index_available = True

    def indexing_bplus_tree_index(self):
        pass
        # self.index_table = bplus_tree()
        # for index, row in enumerate(self.table):
        #     pk = self.table[index].__values__[0]  # primary key = id <=> first element
        #     self.index_table.insert(pk, row.__values__)  # <id,row>
        # self.index_available = True


def create_row(name, attr):  # 表名，attr是一个dict，对应{attr, value}
    # TB
    # print(TB.keys())
    if name not in TB.keys():
        TB[name] = []
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

    if name not in PK.keys():
        PK[name] = cls.__attrs__[0]  # 默认第一个元素为Primary Key
    TB[name].append(cls)


# todo join
TB = {}  # {table_name, table_name_list}
PK = {}  # {table_name, primary_key}

if __name__ == '__main__':
    # test1()
    # test2()
    test_extendible()
