# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : get_relevance.py

import logging

from bin.unit.replaceRelevance import get_value


def get_relevance(data, relevance_list, relevance):
    """
    从返回结果中获取关联值
    :param data:
    :param relevance_list:
    :param relevance:
    :return:
    """
    # 关联键是否时list
    if not relevance_list:
        return relevance
    logging.debug("从返回结果中根据关联键%s提取值" % relevance_list)
    if isinstance(relevance_list, list):
        # 遍历关联键
        for j in relevance_list:
            # 从结果中提取关联键的值
            relevance_value = get_value(data, j)
            print(relevance_value)
            if relevance_value:
                # 考虑到一个关联键，多个值
                if j in relevance:
                    if isinstance(relevance[j], list):
                        a = relevance[j]
                        a.append(relevance_value)
                        relevance[j] = a
                    else:
                        a = relevance[j]
                        b = list()
                        b.append(a)
                        b.append(relevance_value)
                        relevance[j] = b
                else:
                    relevance[j] = relevance_value
            else:
                relevance = relevance_value
    else:
        relevance_value = get_value(data, relevance_list)
        if relevance_value:
            # 考虑到一个关联键，多个值
            if relevance_list in relevance:
                if isinstance(relevance_list, list):
                    a = relevance[relevance_list]
                    a.append(relevance_value)
                    relevance[relevance_list] = a
                else:
                    a = relevance[relevance_list]
                    b = list()
                    b.append(a)
                    b.append(relevance_value)
                    relevance[relevance_list] = a
            else:
                relevance[relevance_list] = relevance_value
    logging.debug("提取后，关联键对象\n%s" % relevance)
    return relevance
