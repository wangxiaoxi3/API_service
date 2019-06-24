# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : ini_request.py

import logging
import time
import allure

from bin.unit.readResultRelevance import get_relevance
from bin.unit.apiSend import send_request


def ini_request(case_dict, _path, relevance=None):
    """
    用例前提条件执行，提取关键值
    :param case_dict: 用例对象
    :param relevance: 关联对象
    :param _path: case路径
    :return:
    """
    if isinstance(case_dict["premise"], list):
        logging.info("执行测试用例前置接口")
        with allure.step("接口关联请求"):
            for i in case_dict["premise"]:
                relevance_list = {}
                for j in range(0, 3):
                    code, data = send_request(i, case_dict["test_info"].get("host"),
                                              i["address"], relevance_list, _path)
                    if not data:
                        with allure.step("接口请求失败！等待三秒后重试！"):
                            pass
                    if i["relevance"]:
                        if len(i["relevance"]):
                            relevance = get_relevance(data, i["relevance"], relevance)
                            print(relevance)
                            if isinstance(relevance, bool):
                                with allure.step("从结果中提取关联键的值失败！等待3秒后重试！"):
                                    pass
                                logging.info("从结果中提取关联键的值失败！等待3秒后重试！")
                                time.sleep(3)
                                continue
                            else:
                                break
                        else:
                            break
                    else:
                        break
                if isinstance(relevance, bool):
                    logging.info("从结果中提取关联键的值失败！重试三次失败")
                    raise Exception("获取前置接口关联数据失败")
    else:
        pass
    return relevance
