# -*- coding: utf-8 -*-  
""" 
@author: DoraVemon
@file: autogen_arith.py 
@time: 2018/10/2 8:45 
"""

import random
import pandas as pd
import numpy as np
from datetime import datetime


def add_test(sum_value, count):
    '''
    返回指定个数（count）的计算题，以计算某数(sum_value）以内的加法
    :param sum_value: 指定某数以内（的加法）
    :param count: 随机生成多少题
    :return: 返回count个计算题
    '''

    questions = []
    count_temp = 0  # 计数器

    while True:
        i = random.randrange(0, sum_value)  # 随机生成 第一个加数
        j = random.randrange(1, sum_value + 1)  # 随机生成 和
        l = j - i  # 第二个加数
        if l > 0:
            # str_temp = str(i) + ' + ' + str(l) + '' + ' =    \n'
            # questions += str_temp
            questions.append((i, l, j))
            count_temp += 1
            if count_temp >= count:
                break
    return questions


def resort(quiz):
    rng_index = random.randint(0, 2)
    flag_addsub = random.randint(0, 1)
    if flag_addsub:
        str_temp = (str(quiz[0]) if rng_index != 0 else '(  )') + ' + ' \
                   + (str(quiz[1]) if rng_index != 1 else '(  )') \
                   + ' = ' \
                   + (str(quiz[2]) if rng_index != 2 else '(  )') + '\n'
    else:
        str_temp = (str(quiz[2]) if rng_index != 0 else '(  )') + ' - ' \
                   + (str(quiz[1]) if rng_index != 1 else '(  )') \
                   + ' = ' \
                   + (str(quiz[0]) if rng_index != 2 else '(  )') + '\n'
    return str_temp


def main():
    sum_value, count = 100, 200  # 随机出20题，10以内的加减法
    #text = ''
    seq=[]
    quizs = add_test(sum_value, count)
    for quiz in quizs:
       seq.append(resort(quiz))
       # text += resort(quiz)
    seq=pd.DataFrame(seq,index=None)
    seq.to_excel('D:/dev/py/C101-'+datetime.now().strftime("_%Y%m%d")+'.xlsx')
    # title = '%d以内加法算术题' % sum_value + datetime.now().strftime("_%Y%m%d") + '.txt'
    # with open(title, "w") as f:
    #     f.write(text)
    # f.close()


if __name__ == '__main__':
    main()