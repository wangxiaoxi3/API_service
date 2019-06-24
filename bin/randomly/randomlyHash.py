# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : md5.py

import hashlib
import re


def md5(data):
    """
    md5加密
    :param data:想要加密的字符
    :return:
    """
    m1 = hashlib.md5()
    m1.update(data.encode("utf-8"))
    data = m1.hexdigest()
    return data


if __name__ == '__main__':
    print(md5("ssss"))
