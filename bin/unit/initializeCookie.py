# -*- coding: utf-8 -*-
# @Time    : 2019/06
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : ini_cookie.py

import os
from setupMain import project_path
from bin.config.confManage import dir_manage


def ini_cookie():
    """
    读取cookie文件
    :return:
    """
    file = project_path + dir_manage('${cookie_dir}$')
    with open(file, 'rb') as f:
        cookie = f.read().decode()

    return cookie.strip("\n")
