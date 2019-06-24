# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : read_param.py

import json

from json import JSONDecodeError
from bin.unit.replaceRelevance import replace


def read_param(test_name, param, _path, relevance=None):
    """
    读取用例中参数parameter
    :param test_name: 用例名称
    :param param: parameter
    :param relevance: 关联对象
    :param _path: case路径
    :param result: 全局结果
    :return:
    """

    if isinstance(param, dict):
        param = replace(param, relevance)
    elif isinstance(param, list):
        param = replace(param, relevance)
    elif param is None:
        pass
    else:
        try:
            with open(_path + "/" + param, "r", encoding="utf-8") as f:
                data = json.load(f)
                for i in data:
                    if i["test_name"] == test_name:
                        param = i["parameter"]
                        break
                if not isinstance(param, dict):
                    raise Exception("未能找到用例关联的参数\n文件路径：%s\n索引：%s" % (param, _path))
                else:
                    param = replace(param, relevance)
        except FileNotFoundError:
            raise Exception("用例关联文件不存在\n文件路径： %s" % param)
        except JSONDecodeError:
            raise Exception("用例关联的参数文件有误\n文件路径： %s" % param)
    return param










