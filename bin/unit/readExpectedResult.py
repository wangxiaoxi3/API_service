# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : read_json.py

import json
from json import JSONDecodeError

from bin.unit.replaceRelevance import replace


def read_json(test_names, code_json, _path, relevance=None):
    """
    校验内容读取
    :param test_names: 用例名称
    :param code_json: 文件路径
    :param relevance: 关联对象
    :param _path: case路径
    :return:
    """
    if isinstance(code_json, dict):
        code_json = replace(code_json, relevance)
    else:
        try:
            with open(_path+'/'+code_json, "r", encoding="utf-8") as file:
                data = json.load(file)
                for i in data:
                    if i['test_name'] == test_names:
                        code_json = i['json']
                        break
                if not code_json:
                    raise Exception("未找到用例关联的期望结果\n文件路径： %s\n索引： %s" % (code_json, test_names))
                else:
                    code_json = replace(code_json, relevance)
        except FileNotFoundError:
            raise Exception("用例关联文件不存在\n文件路径： %s" % code_json)
        except JSONDecodeError:
            raise Exception("用例关联的期望文件有误\n文件路径： %s" % code_json)

    return code_json



