# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : setup.py

import os


import pytest
from bin.config.confManage import dir_manage
from bin.script.logs import LogConfig
project_path = os.path.split(os.path.realpath(__file__))[0]

if ':' in project_path:
    project_path = project_path.replace('\\', '/')
else:
    pass


if __name__ == '__main__':
    LogConfig(project_path)
    from bin.script.writeCase import write_case
    write_case(project_path + dir_manage('${data_dir}$'))
    args = ['-s', '-q', '--alluredir', project_path + dir_manage('${report_xml_dir}$')]
    pytest.main(args)
    cmd = 'allure generate %s -o %s -c' % (project_path + dir_manage('${report_xml_dir}$'),
                                           project_path + dir_manage('${report_html_dir}$'))
    os.system(cmd)

