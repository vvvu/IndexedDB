import random
import string


class random_data():
    def lowercase_string(self, n = 5):
        '''
        :param n: 随机生成的单词长度
        :return:
        '''
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(n))

    def uppercase_string(self, n = 5):
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(n))

    def ascil_string(self, n = 5):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(n))


def gen(attr_list: list, num):
    '''
    输入文件第一行：attr
    第二行至末尾行：row
    '''
    attrs = '\t'.join(attr_list)
    rdgen = random_data()
    idx = 0
    with open('gen_data.txt', 'w', encoding = 'utf-8') as f:
        for idx in range(0, num + 1):
            s = ""
            if idx == 0:
                s = attrs
            else:
                s = '\t'.join([str(idx),rdgen.lowercase_string(5),rdgen.uppercase_string(7),rdgen.ascil_string(9)])
            f.write(s + '\n')


gen(['id', 'str1', 'str2', 'str3'], 10000)
