# api_service
#### 简介：

基于Pytest+request+Allure的接口自动化框架；
主要应用于Affiliate接口测试，其他项目也可看情况应用。

----
#### 接口文件:

备注：Charles导出接口应选择文件类型为`JSON Session File(.chlsj)`

----
#### 模块类的设计:
备注：Charles导出接口应选择文件类型为`JSON Session File(.chlsj)`\
重要模块介绍：
>1、writeCase.py ：自动读取新的Charles文件，并自动生成测试用例 \
 2、apiMethod.py：封装request方法，可以支持多协议扩展（get\post\put\delete）\
 3、checkResult.py：封装验证response方法\
 4、setupMain.py： 核心代码，定义并执行用例集，生成报告

----

详细介绍见原文: https://www.jianshu.com/p/6f5bfc1182ae

