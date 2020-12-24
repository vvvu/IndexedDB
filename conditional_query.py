def equal(self, attr, value):
    query_table = []  # 查询结果
    for index, row in enumerate(self.table):  # 顺序查找
        if str(row.__dict__[attr]) == str(value):
            query_table.append(row)
    return query_table


def not_equal(self, attr, value):
    query_table = []
    for index, row in enumerate(self.table):
        if str(row.__dict__[attr]) != str(value):
            query_table.append(row)
    return query_table


def geq(self, attr, value):
    query_table = []
    for index, row in enumerate(self.table):
        if str(row.__dict__[attr]) >= str(value):
            query_table.append(row)
    return query_table


def gt(self, attr, value):
    query_table = []
    for index, row in enumerate(self.table):
        if str(row.__dict__[attr]) > str(value):
            query_table.append(row)
    return query_table


def leq(self, attr, value):
    query_table = []
    for index, row in enumerate(self.table):
        if str(row.__dict__[attr]) <= str(value):
            query_table.append(row)
    return query_table


def lt(self, attr, value):
    query_table = []
    for index, row in enumerate(self.table):
        if str(row.__dict__[attr]) < str(value):
            query_table.append(row)
    return query_table


def between_and(self, attr, value: tuple):
    query_table = []
    lb, ub = value[0], value[1]
    for index, row in enumerate(self.table):
        if str(lb) < str(row.__dict__[attr]) < str(ub):
            query_table.append(row)
    return query_table