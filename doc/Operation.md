## 系统环境准备：

1、jdk1.8以上
2、allure==2.13
3、python3.8
4、Charles

## python环境：
pytest==5.4.0
allure-pytest==2.8.15
allure-python-commons==2.8.15
pytest-rerunfailures==9.0
allure-python-commons==2.8.15
configparser==5.0.0
PyYAML==5.3.1
requests==2.23.0
requests-toolbelt==0.9.1
simplejson==3.17.0
ruamel.yaml==0.16.10

## 配置步骤：
1、git clone 代码到本地
2、修改/bin/config/config.ini,directory中将CRM修改为对应项目目录
3、使用Charles录制对应接口数据，export到本地，文件类型为JSON Session File(.chlsj)
4、接口文件放在config.ini中data_dir目录
5、运行setupMain.py
