# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : random_string.py

import random
import string


def random_string(num_len):
    """
    从a-zA-Z0-9生成制定数量的随机字符
    :param num_len: 字符串长度
    :return:
    """
    try:
        num_len = int(num_len)
    except ValueError:
        raise Exception("从a-zA-Z0-9生成指定数量的随机字符失败！长度参数有误  %s" % num_len)
    strings = ''.join(random.sample(string.hexdigits, +num_len))
    return strings


if __name__ == '__main__':
    print(random_string(16))
