# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service

import re
from bin.config.confRead import Config


def host_manage(hos):
    """
    host关联配置
    :param hos:
    :return:
    """
    try:
        relevance_list = re.findall(r'\${(.*?)}\$', hos)
        for n in relevance_list:
            pattern = re.compile(r'\${' + n + r'}\$')
            host_cf = Config()
            host_relevance = host_cf.read_host()
            hos = re.sub(pattern, host_relevance[n], hos, count=1)
    except TypeError:
        pass
    return hos


def mail_manage(ml):
    """
    email关联配置
    :param ml:
    :return:
    """
    try:
        relevance_list = re.findall(r"\${(.*?)}\$", ml)
        for n in relevance_list:
            pattern = re.compile(r'\${' + n + r'}\$')
            email_cf = Config()
            email_relevance = email_cf.read_email()
            ml = re.sub(pattern, email_relevance[n], ml, count=1)
    except TypeError:
        pass
    return ml


def dir_manage(directory):
    """
    directory关联配置
    :param directory:
    :return:
    """
    try:
        relevance_list = re.findall(r"\${(.*?)}\$", directory)
        for n in relevance_list:
            pattern = re.compile(r'\${' + n + r'}\$')
            dir_cf = Config()
            dir_relevance = dir_cf.read_dir()
            directory = re.sub(pattern, dir_relevance[n], directory, count=1)
    except TypeError:
        pass
    return directory


if __name__ == '__main__':
    host = host_manage(hos='${pre}$')
    dirs = dir_manage(directory='${case_dir}$')

    print(host)
    print(dirs)
