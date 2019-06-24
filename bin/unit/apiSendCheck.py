# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : apiSendCheck.py


from bin.unit import checkResult, apiSend
from bin.unit.readResultRelevance import get_relevance


def api_send_check(case, project_dict, relevance, _path, rel=None):
    """
    接口请求并校验结果
    :param case: 单条用例
    :param project_dict: 用例文件对象
    :param relevance: 关键值实例对象
    :param rel: 关联值类对象
    :param _path: case目录
    :return:
    """
    code, data = apiSend.send_request(case, project_dict["test_info"].get("host"),
                                      project_dict["test_info"].get("address"), _path, relevance)
    if isinstance(case["check"], list):
        for i in case["check"]:
            checkResult.check_result(case["test_name"], i, code, data, _path, relevance)
    else:
        checkResult.check_result(case["test_name"], case["check"], code, data, _path, relevance)

    get_relevance(data, case["relevance"], rel)



