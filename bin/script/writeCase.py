# -*- coding: utf-8 -*-
# @Time    : 2019/06
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : writeCase.py

import os
import shutil
from bin.script.mkDir import mk_dir

from bin.script.writeCaseYml import write_case_yml


def write_case(_path):
    yml_list = write_case_yml(_path)
    project_path = str(os.path.abspath('.').split('/bin')[0])
    test_path = project_path+'/aff/testcase/'
    src = test_path+'Template.py'

    for case in yml_list:
        yml_path = case.split('/')[0]
        yml_name = case.split('/')[1]
        case_name = 'test_' + yml_name + '.py'
        new_case = test_path + yml_path + '/' + case_name
        mk_dir(test_path + yml_path)
        if case_name in os.listdir(test_path + yml_path):
            pass
        else:
            shutil.copyfile(src, new_case)
            with open(new_case, 'r') as fw:
                source = fw.readlines()
            n = 0
            with open(new_case, 'w') as f:
                for line in source:
                    if 'PATH = setupMain.PATH' in line:
                        line = line.replace("/aff/page/offer", "/aff/page/%s" % yml_path)
                        f.write(line)
                        n = n+1
                    elif 'case_dict = ini_case' in line:
                        line = line.replace("Template", yml_name)
                        f.write(line)
                        n = n + 1
                    elif 'class TestTemplate' in line:
                        line = line.replace("TestTemplate", "Test%s" % yml_name.title().replace("_", ""))
                        f.write(line)
                        n = n + 1
                    elif '@allure.story' in line:
                        line = line.replace("Template", yml_name)
                        f.write(line)
                        n = n + 1
                    elif 'def test_template' in line:
                        line = line.replace("template", yml_name.lower())
                        f.write(line)
                        n = n + 1

                    else:
                        f.write(line)
                        n += 1
                for i in range(n, len(source)):
                    f.write(source[i])


if __name__ == '__main__':
    ym_path = '/Users/workpace/Aff_service_git/aff/data'
    write_case(ym_path)

