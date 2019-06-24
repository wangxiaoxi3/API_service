# -*- coding: utf-8 -*-
# @Time    : 2019/06
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : ini_cookie.py

import os
import setupMain


def ini_cookie():
    """
    读取cookie文件
    :return:
    """
    file = setupMain.PATH + '/aff/data/cookie.txt'
    with open(file, 'rb') as f:
        cookie = f.read().decode()

    return cookie.strip("\n")
