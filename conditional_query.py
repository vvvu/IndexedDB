'''
Normal conditional query
'''


def equal(self, attr, value):
    query_table = []  # 查询结果
    for index, row in enumerate(self.TB[self.table_name]):  # 顺序查找
        if str(row.__dict__[attr]) == str(value):
            query_table.append(row)
    return query_table


def not_equal(self, attr, value):
    query_table = []
    for index, row in enumerate(self.TB[self.table_name]):
        if str(row.__dict__[attr]) != str(value):
            query_table.append(row)
    return query_table


def geq(self, attr, value):
    query_table = []
    for index, row in enumerate(self.TB[self.table_name]):
        if str(row.__dict__[attr]) >= str(value):
            query_table.append(row)
    return query_table


def gt(self, attr, value):
    query_table = []
    for index, row in enumerate(self.TB[self.table_name]):
        if str(row.__dict__[attr]) > str(value):
            query_table.append(row)
    return query_table


def leq(self, attr, value):
    query_table = []
    for index, row in enumerate(self.TB[self.table_name]):
        if str(row.__dict__[attr]) <= str(value):
            query_table.append(row)
    return query_table


def lt(self, attr, value):
    query_table = []
    for index, row in enumerate(self.TB[self.table_name]):
        if str(row.__dict__[attr]) < str(value):
            query_table.append(row)
    return query_table


def between_and(self, attr, value: tuple):
    query_table = []
    lb, ub = value[0], value[1]
    for index, row in enumerate(self.TB[self.table_name]):
        if str(lb) < str(row.__dict__[attr]) < str(ub):
            query_table.append(row)
    return query_table


# Indexing search
def indexing_search(self, attr, pk):
    assert self.index_available == True, "No available indexing"
    indexs = []
    idx = self.index_table.get(pk)
    indexs.append(idx)
    return indexs

'''
def linear_search(self, attr, pk):
    assert self.index_available == True, "No available linear index"
    indexs = []
    idx = self.index_table.get(pk)
    indexs.append(idx)
    return indexs

def extendible_search(self, attr, pk):
    assert self.index_available == True, "No available extendible index"
    indexs = []
    idx = self.index_table.get(pk)
    indexs.append(idx)
    return indexs


def bplus_search(self, attr, pk):
    assert self.index_available == True, "No available bplus index"
    pass
'''