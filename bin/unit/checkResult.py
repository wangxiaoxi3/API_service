# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : check_result.py

import operator
import re
import allure

from bin.unit import readExpectedResult


def check_json(src_data, dst_data):
    """
    校验的json
    :param src_data: 检验内容
    :param dst_data: 接口返回的数据
    :return:
    """
    if isinstance(src_data, dict):
        for key in src_data:
            if key not in dst_data:
                raise Exception("JSON格式校验，关键字%s不在返回结果%s中" % (key, dst_data))
            else:
                this_key = key
                if isinstance(src_data[this_key], dict) and isinstance(dst_data[this_key], dict):
                    check_json(src_data[this_key], dst_data[this_key])
                elif isinstance(type(src_data[this_key]), type(dst_data[this_key])):
                    raise Exception("JSON格式校验，关键字 %s 与 %s 类型不符" % (src_data[this_key], dst_data[this_key]))
                else:
                    pass
    else:
        raise Exception("JSON校验内容非dict格式")


def check_result(test_name, case, code, data, _path, relevance=None):
    """
    校验测试结果
    :param test_name: 测试名称
    :param case: 测试用例
    :param code: HTTP状态
    :param data: 返回的接口json数据
    :param relevance: 关联值对象
    :param _path: case路径
    :return:
    """

    if case["check_type"] == 'no_check':
        with allure.step("不校验结果"):
            pass
    elif case["check_type"] == 'json':
        expected_request = case["expected_request"]
        if isinstance(case["expected_request"], str):
            expected_request = readExpectedResult.read_json(test_name, expected_request, _path, relevance)
        with allure.step("JSON格式校验"):
            allure.attach(name="期望code", body=str(case["expected_code"]))
            allure.attach(name='期望data', body=str(expected_request))
            allure.attach(name="实际code", body=str(code))
            allure.attach(name='实际data', body=str(data))
        if int(code) == case["expected_code"]:
            if not data:
                data = "{}"
            check_json(expected_request, data)
        else:
            raise Exception("http状态码错误！\n %s != %s" % (code, case["expected_code"]))

    elif case["check_type"] == 'only_check_status':
        with allure.step("校验HTTP状态"):
            allure.attach(name="期望code", body=str(case["expected_code"]))
            allure.attach(name="实际code", body=str(code))
            allure.attach(name='实际data', body=str(data))
        if int(code) == case["expected_code"]:
            pass
        else:
            raise Exception("http状态码错误！\n %s != %s" % (code, case["expected_code"]))

    elif case["check_type"] == 'entirely_check':
        expected_request = case["expected_request"]
        if isinstance(case["expected_request"], str):
            expected_request = readExpectedResult.read_json(test_name, expected_request, _path, relevance)
        with allure.step("完全校验"):
            allure.attach(name="期望code", body=str(case["expected_code"]))
            allure.attach(name='期望data', body=str(expected_request))
            allure.attach(name="实际code", body=str(code))
            allure.attach(name='实际data', body=str(data))
        if int(code) == case["expected_code"]:
            result = operator.eq(expected_request, data)
            if result:
                pass
            else:
                raise Exception("完全校验失败！ %s ! = %s" % (expected_request, data))
        else:
            raise Exception("http状态码错误！\n %s != %s" % (code, case["expected_code"]))

    elif case["check_type"] == 'Regular_check':
        if int(code) == case["expected_code"]:
            try:
                result = ""
                if isinstance(case["expected_request"], list):
                    for i in case[""]:
                        result = re.findall(i.replace("\"", "\""), str(data))
                        allure.attach('校验完成结果\n', str(result))
                else:
                    result = re.findall(case["expected_request"].replace("\"", "\'"), str(data))
                    with allure.step("正则校验"):
                        allure.attach(name="期望code", body=str(case["expected_code"]))
                        allure.attach(name='正则表达式', body=str(case["expected_request"]).replace("\'", "\""))
                        allure.attach(name="实际code", body=str(code))
                        allure.attach(name='实际data', body=str(data))
                        allure.attach(name=case["expected_request"].replace("\"", "\'") + '校验完成结果',
                                      body=str(result).replace("\'", "\""))
                if not result:
                    raise Exception("正则未校验到内容！ %s" % case["expected_request"])
            except KeyError:
                raise Exception("正则校验执行失败！ %s\n正则表达式为空时" % case["expected_request"])
        else:
            raise Exception("http状态码错误！\n %s != %s" % (code, case["expected_code"]))

    else:
        raise Exception("无该校验方式%s" % case["check_type"])
