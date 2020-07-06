# -*- coding: utf-8 -*-
# @Time    : 2019/06
# @Author  : XiaoXi
# @PROJECT : Aff_service

import allure
import pytest
from setupMain import project_path
from bin.config.confManage import dir_manage
from bin.unit.initializeCase import ini_case
from bin.unit.initializePremise import ini_request
from bin.unit.apiSendCheck import api_send_check

PATH = project_path + dir_manage('${page_dir}$') + "offer"

case_dict = ini_case(PATH, "Template")


@allure.feature(case_dict["test_info"]["title"])
class TestTemplate:

    @pytest.mark.parametrize("case_data", case_dict["test_case"], ids=[])
    @allure.story("Template")
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_template(self, case_data):
        """

        :param case_data: 测试用例
        :return:
        """
        self.init_relevance = ini_request(case_dict, PATH)
        # 发送测试请求
        api_send_check(case_data, case_dict, self.init_relevance, PATH)


