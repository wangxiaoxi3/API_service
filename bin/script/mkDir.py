# -*- coding: utf-8 -*-
# @Time    : 2019/06
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : Mkdir.py

import os
import logging


def mk_dir(path):
    # 去除首位空格
    path = path.strip()
    path = path.rstrip("\\")
    path = path.rstrip("/")

    # 判断路径是否存在
    is_exists = os.path.exists(path)

    if not is_exists:
        try:
            os.makedirs(path)
        except Exception as e:
            logging.error("logs目录创建失败：%s" % e)
    else:
        # 如果目录存在则不创建，并提示目录已存在
        logging.debug("logs目录已存在：%s" % str(path))
        pass
