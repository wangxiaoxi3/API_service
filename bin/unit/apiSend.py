# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : send_request.py

import logging
import allure

from bin.unit import apiMethod, replaceRelevance
from bin.unit import initializeCookie
from bin.config import confManage
from bin.unit import readParameter


def send_request(data, host, address, _path, relevance=None):
    """
    封装请求
    :param data: 测试用例
    :param host: 测试host
    :param address: 接口地址
    :param relevance: 关联对象
    :param _path: case路径
    :return:
    """
    logging.info("="*100)
    header = readParameter.read_param(data["test_name"], data["headers"], _path, relevance)
    if data["cookies"] is True:
        header["Cookie"] = initializeCookie.ini_cookie()
    logging.debug("请求头处理结果：%s" % header)
    parameter = readParameter.read_param(data["test_name"], data["parameter"], _path, relevance)
    logging.debug("请求参数处理结果：%s" % parameter)
    try:
        host = data["host"]
    except KeyError:
        pass
    try:
        address = data["address"]
    except KeyError:
        pass
    host = confManage.host_manage(host)
    address = replaceRelevance.replace(address, relevance)
    logging.debug("host处理结果： %s" % host)
    if not host:
        raise Exception("接口请求地址为空 %s" % data["headers"])
    logging.info("请求接口：%s" % str(data["test_name"]))
    logging.info("请求地址：%s" % data["http_type"] + "://" + host + address)
    logging.info("请求头: %s" % str(header))
    logging.info("请求参数: %s" % str(parameter))
    if data["test_name"] == 'password正确':
        with allure.step("保存cookie信息"):
            allure.attach(name="请求接口", body=str(data["test_name"]))
            allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
            allure.attach(name="请求头", body=str(header))
            allure.attach(name="请求参数", body=str(parameter))
            apiMethod.save_cookie(header=header, address=data["http_type"] + "://" + host + address, data=parameter)

    if data["request_type"].lower() == 'post':
        logging.info("请求方法: POST")
        if data["file"]:
            with allure.step("POST上传文件"):
                allure.attach(name="请求接口", body=str(data["test_name"]))
                allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
                allure.attach(name="请求头", body=str(header))
                allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.post(header=header,
                                    address=data["http_type"] + "://" + host + address,
                                    request_parameter_type=data["parameter_type"],
                                    files=parameter,
                                    timeout=data["timeout"])
        else:
            with allure.step("POST请求接口"):
                allure.attach(name="请求接口", body=str(data["test_name"]))
                allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
                allure.attach(name="请求头", body=str(header))
                allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.post(header=header,
                                    address=data["http_type"] + "://" + host + address,
                                    request_parameter_type=data["parameter_type"],
                                    data=parameter,
                                    timeout=data["timeout"])
    elif data["request_type"].lower() == 'get':
        with allure.step("GET请求接口"):
            allure.attach(name="请求接口", body=str(data["test_name"]))
            allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
            allure.attach(name="请求头", body=str(header))
            allure.attach(name="请求参数", body=str(parameter))
            logging.info("请求方法: GET")
        result = apiMethod.get(header=header,
                               address=data["http_type"] + "://" + host + address,
                               data=parameter,
                               timeout=data["timeout"])
    elif data["request_type"].lower() == 'put':
        logging.info("请求方法: PUT")
        if data["file"]:
            with allure.step("PUT上传文件"):
                allure.attach(name="请求接口", body=str(data["test_name"]))
                allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
                allure.attach(name="请求头", body=str(header))
                allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.put(header=header,
                                   address=data["http_type"] + "://" + host + address,
                                   request_parameter_type=data["parameter_type"],
                                   files=parameter,
                                   timeout=data["timeout"])
        else:
            with allure.step("PUT请求接口"):
                allure.attach(name="请求接口", body=str(data["test_name"]))
                allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
                allure.attach(name="请求头", body=str(header))
                allure.attach(name="请求参数", body=str(parameter))
            result = apiMethod.put(header=header,
                                   address=data["http_type"] + "://" + host + address,
                                   request_parameter_type=data["parameter_type"],
                                   data=parameter,
                                   timeout=data["timeout"])
    elif data["request_type"].lower() == 'delete':
        with allure.step("DELETE请求接口"):
            allure.attach(name="请求接口", body=str(data["test_name"]))
            allure.attach(name="请求地址", body=data["http_type"] + "://" + host + address)
            allure.attach(name="请求头", body=str(header))
            allure.attach(name="请求参数", body=str(parameter))
        logging.info("请求方法: DELETE")
        result = apiMethod.delete(header=header,
                                  address=data["http_type"] + "://" + host + address,
                                  data=parameter,
                                  timeout=data["timeout"])
    else:
        result = {"code": False, "data": False}
    logging.info("请求接口结果：\n %s" % str(result))
    return result
