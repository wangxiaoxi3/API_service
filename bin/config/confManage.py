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
        relevance_list = re.findall("\${(.*?)}\$", hos)
        for n in relevance_list:
            pattern = re.compile('\${' + n + '}\$')
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
        relevance_list = re.findall("\${(.*?)}\$", ml)
        for n in relevance_list:
            pattern = re.compile('\${' + n + '}\$')
            email_cf = Config()
            email_relevance = email_cf.read_email()
            ml = re.sub(pattern, email_relevance[n], ml, count=1)
    except TypeError:
        pass
    return ml


if __name__ == '__main__':
    host = host_manage(hos='${debug_pre}$')
    email = mail_manage(ml='${smtpserver}$')
    print(host)
    print(email)
