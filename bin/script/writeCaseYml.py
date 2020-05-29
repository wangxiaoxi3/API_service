# -*- coding: utf-8 -*-
# @Time    : 2019/06
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : writeCaseYml.py

import json
import os
import urllib.parse
import logging
from ruamel import yaml
from bin.script.mkDir import mk_dir
from setupMain import project_path
from bin.config.confManage import dir_manage


def write_case_yml(har_path):
    """
    循环读取导出文件
    :param har_path: Charles导出文件路径
    :return:
    """
    har_list = os.listdir(har_path)
    case_file_list = []

    for i in har_list:
        if 'chlsj' in i:
            with open(har_path+'/'+str(i), 'r', encoding='utf-8') as f:
                logging.debug("从%s目录下，读取文件%s" % (har_path, i))

                har_cts = json.loads(f.read())
                har_ct = har_cts[0]
                case_list = dict()
                scheme = har_ct["scheme"]
                method = har_ct["method"]
                path = har_ct["path"]
                title = path.split("/")[-1]
                info_id = "test_" + title + "_01"
                parameter_type = har_ct["request"]["mimeType"]
                parameter = dict()
                try:
                    if method in 'POST':
                        parameter_list = urllib.parse.unquote(har_ct["request"]["body"]["text"])
                    elif method in 'PUT':
                        parameter_list = har_ct["request"]["body"]["text"]
                    elif method in 'DELETE':
                        parameter_list = urllib.parse.unquote(har_ct["request"]["body"]["text"])
                    else:
                        parameter_list = har_ct["query"]

                    if "&" in parameter_list:

                        for key in parameter_list.split("&"):
                            val = key.split("=")
                            parameter[val[0]] = val[1]
                    else:
                        parameter = json.loads(parameter_list)
                except Exception as e:
                    logging.error("未找到parameter: %s" % e)
                    raise e

                case_path = project_path + dir_manage('${page_dir}$') + path.split("/")[-2]
                mk_dir(case_path)

                response_code = har_ct["response"]["status"]
                response_body = har_ct["response"]["body"]["text"]
                test_info = dict()
                test_info["id"] = info_id
                test_info["title"] = path.split("/")[-2]
                test_info["host"] = '${host}$'
                test_info["address"] = path

                # 定义checkout
                check = dict()
                check["check_type"] = 'json'
                check["expected_code"] = response_code
                expected_request = json.loads(response_body)

                result_file = 'result_' + title + '.json'
                # result参数大于4时，写入result.json中
                if len(expected_request) >= 2:
                    if result_file in os.listdir(case_path):
                        pass
                    else:
                        result_list = []
                        result_dicts = dict()
                        with open(case_path + '/' + result_file, "w", encoding='utf-8') as ff:
                            result_dicts["test_name"] = title
                            result_dicts["json"] = expected_request
                            result_list.append(result_dicts)

                            json.dump(result_list, ff, ensure_ascii=False, indent=4)
                    check["expected_request"] = result_file

                else:
                    check["expected_request"] = expected_request

                param_file = case_path + '/' + title + '.json'
                test_case_list = []
                test_case = dict()
                test_case_list.append(test_case)
                # para参数大于等于4时，参数文件单独写入json中
                if len(parameter) >= 4:
                    if title + '.json' in os.listdir(case_path):
                        pass
                    else:
                        new_dicts = dict()
                        new_list = []
                        with open(param_file, "w", encoding='utf-8') as fs:
                            new_dicts["test_name"] = title
                            new_dicts["parameter"] = parameter
                            new_list.append(new_dicts)

                            json.dump(new_list, fs, ensure_ascii=False, indent=4)

                    test_case["test_name"] = title
                    test_case["info"] = title
                    test_case["http_type"] = scheme
                    test_case["request_type"] = method
                    test_case["parameter_type"] = parameter_type
                    test_case["address"] = path
                    test_case["headers"] = {"X-Requested-With": "XMLHttpRequest"}
                    test_case["cookies"] = True
                    test_case["timeout"] = 20
                    test_case["parameter"] = title + '.json'
                    test_case["file"] = False
                    test_case["check"] = check
                    test_case["relevance"] = None

                else:
                    test_case["test_name"] = title
                    test_case["info"] = title
                    test_case["http_type"] = scheme
                    test_case["request_type"] = method
                    test_case["parameter_type"] = parameter_type
                    test_case["address"] = path
                    test_case["headers"] = {"X-Requested-With": "XMLHttpRequest"}
                    test_case["cookies"] = True
                    test_case["timeout"] = 20
                    test_case["parameter"] = parameter
                    test_case["file"] = False
                    test_case["check"] = check
                    test_case["relevance"] = None

                case_list["test_info"] = test_info
                case_list["premise"] = None
                case_list["test_case"] = test_case_list

                case_file = case_path + '/' + title + '.yml'
                if title + '.yml' in os.listdir(case_path):
                    pass
                else:
                    with open(case_path + '/' + title + '.yml', 'w+', encoding='utf-8') as ff:
                        case_file_list.append(path.split("/")[-2]+'/'+title)
                        logging.debug("从%s目录下，写入测试文件%s" % (case_path, case_file))
                        yaml.dump(case_list, ff, Dumper=yaml.RoundTripDumper)
    return case_file_list


if __name__ == '__main__':
    har = '/Users/wangjuan/workpace/api_service/crm/data'
    s = write_case_yml(har)
