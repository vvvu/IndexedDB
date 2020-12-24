from main import *


def test1():
    attr = ['id', 'name', 'sex', 'major', 'age', 'birthday', 'contact', 'credit']  # student 的属性
    fp = 'student.txt'
    with open(fp, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip().split('\t')
            d = {attr[i]: line[i] for i in range(0, len(attr))}  # 字典：映射属性和属性值
            create_row('student', d)  # 在student表中加入对应项

    q = query('student')
    query_result = q.search('age', (15, 20), between_and)  # 查询年龄在(15,20) 的人
    q.print(query_result, head=10)  # 输出结果表中前10项

    # print(PK) {Table : Primary Key}


def test2():  # 列筛选
    attr = ['id', 'name', 'sex', 'major', 'age', 'birthday', 'contact', 'credit']  # student 的属性
    fp = 'student.txt'
    with open(fp, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line.strip().split('\t')
            d = {attr[i]: line[i] for i in range(0, len(attr))}  # 字典：映射属性和属性值
            create_row('student', d)  # 在student表中加入对应项

    q = query('student')
    query_result = q.search('age', 15, geq)  # 查询 >= 15岁的人
    q.print(query_result, head=10, cols=['id', 'name'])  # 输出结果表中前10项
