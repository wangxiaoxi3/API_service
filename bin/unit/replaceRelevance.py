# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : replace_relevance.py


import re
# from bin.unit.initializeCase import ini_case


def replace(param, relevance=None):
    """
    替换关联数据
    :param param: 请求参数
    :param relevance: 关联对象
    :return:
    """
    if isinstance(param, dict):
        for key, value in param.items():
            if isinstance(value, dict):
                param[key] = replace(value, relevance)
            elif isinstance(value, list):
                for k, i in enumerate(value):
                    param[key][k] = replace(i, relevance)
            else:
                try:
                    relevance_list = re.findall(r"\${(.*?)}\$", value)

                    relevance_index = 0
                    for n in relevance_list:
                        pattern = re.compile(r'\${' + n + r'}\$')
                        n = n.lower()
                        try:
                            if isinstance(relevance[n], list):
                                try:
                                    param[key] = re.sub(pattern, relevance[n][relevance_index], param[key], count=1)
                                    relevance_index += 1
                                except IndexError:
                                    relevance_index = 0
                                    param[key] = re.sub(pattern, relevance[n][relevance_index], param[key], count=1)
                                    relevance_index += 1
                            else:
                                param[key] = re.sub(pattern, relevance[n], param[key], count=1)
                        except KeyError:
                            pass
                except TypeError:
                    pass
                try:
                    param[key] = param[key]
                except TypeError:
                    pass

    elif isinstance(param, list):
        for k, i in enumerate(param):
            param[k] = replace(i, relevance)
    else:
        try:
            relevance_list = re.findall(r"\${(.*?)}\$", param)
            relevance_index = 0
            for n in relevance_list:
                pattern = re.compile(r'\${' + n + r'}\$')
                try:
                    if isinstance(relevance[n], list):
                        try:
                            param = re.sub(pattern, relevance[n][relevance_index], param, count=1)
                            relevance_index += 1
                        except IndexError:
                            relevance_index = 0
                            param = re.sub(pattern, relevance[n][relevance_index], param, count=1)
                            relevance_index += 1
                    else:
                        param = re.sub(pattern, relevance[n], param)
                except KeyError:
                    pass
        except TypeError:
            pass

    return param


__relevance = ""


def get_value(data, value):
    """
    获取json中的值
    :param data: json数据
    :param value: 值
    :return:
    """
    global __relevance
    if isinstance(data, dict):
        if value in data:
            __relevance = data[value]
        else:
            for key in data:
                __relevance = get_value(data[key], value)
    elif isinstance(data, list):
        for key in data:
            if isinstance(key, dict):
                __relevance = get_value(key, value)
                break
    return __relevance
