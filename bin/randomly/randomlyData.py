# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : choice.py

import random


def choice_data(data):
    """
    获取随机整型数据
    :param data: 数组
    :return:
    """
    _list = data.split(",")
    num = random.choice(_list)
    return num


if __name__ == "__main__":
    print(choice_data("400,100,2"))
