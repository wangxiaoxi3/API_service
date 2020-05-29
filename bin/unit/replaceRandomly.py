# -*- coding: utf-8 -*-
# @Time    : 2019/05
# @Author  : XiaoXi
# @PROJECT : Aff_service
# @File    : replace_random.py

import re

from bin.randomly import randomly_float, randomly_int, randomly_string, randomly_time, randomly_data


def replace_random(value):
    """
    调用定义方法替换字符串
    :param value:
    :return:
    """
    int_list = re.findall(r'\$RandomInt\(([0-9]*,[0-9]*?)\)\$', value)
    string_list = re.findall(r'\$RandomString\(([0-9]*?)\)\$', value)
    float_list = re.findall(r'\$RandomFloat\(([0-9]*,[0-9]*,[0-9]*)\)\$', value)
    time_list = re.findall(r"\$GetTime\(time_type=(.*?),layout=(.*?),unit=([0-9],[0-9],[0-9],[0-9],[0-9])\)\$", value)
    choice_list = re.findall(r"\$Choice\((.*?)\)\$", value)

    if len(int_list):
        # 获取整型数据替换
        for i in int_list:
            pattern = re.compile(r'\$RandomInt\(' + i + r'\)\$')
            key = str(randomly_int.random_int(i))
            value = re.sub(pattern, key, value, count=1)
        value = replace_random(value)

    elif len(string_list):
        # 获取字符串数据替换
        for j in string_list:
            pattern = re.compile(r'\$RandomString\(' + j + r'\)\$')
            key = str(randomly_string.random_string(j))
            value = re.sub(pattern, key, value, count=1)
        value = replace_random(value)

    elif len(float_list):
        # 获取浮点数数据替换
        for n in float_list:
            pattern = re.compile(r'\$RandomFloat\(' + n + r'\)\$')
            key = str(randomly_float.random_float(n))
            value = re.sub(pattern, key, value, count=1)
        value = replace_random(value)

    elif len(time_list):
        # 获取时间替换
        for m in time_list:
            if len(m[0]) and len(m[1]):
                pattern = re.compile(r'\$GetTime\(time_type=' + m[0] + ',layout=' + m[1] + ',unit=' + m[2] + '\)\$')
                key = str(randomly_time.get_time(m[0], m[1], m[2]))
                value = re.sub(pattern, key, value, count=1)
            else:
                print("$GetTime$参数错误，time_type, layout为必填")
        value = replace_random(value)

    elif len(choice_list):
        # 调用choice方法
        for i in choice_list:
            pattern = re.compile(r'\$Choice\(' + i + r'\)\$')
            key = str(randomly_data.choice_data(i))
            value = re.sub(pattern, key, value, count=1)
        value = replace_random(value)

    else:
        pass
    return value


if __name__ == '__main__':
    int_num = '$RandomInt($RandomInt(2,13)$,$RandomInt(2,13)$)$'
    str_num = '$RandomString($RandomInt(2,23)$)$'
    float_num = '$RandomFloat($RandomInt(2,13)$,$RandomInt(2,13)$,$RandomInt(2,13)$)$'
    time_num = '$GetTime(time_type=else,layout=13timestamp,unit=0,0,0,0,6)$'
    choice_num = '$Choice($RandomInt(2,13)$,$RandomInt(2,13)$)$'
    print(replace_random(int_num))
    print(replace_random(str_num))
    print(replace_random(float_num))
    print(replace_random(time_num))
    print(replace_random(choice_num))
