# Aff_service_git
#### 简介：
基于Pytest+request+Allure的接口自动化开源框架2（升级版）

----
#### 模块类的设计:
备注：Charles导出接口应选择文件类型为`JSON Session File(.chlsj)`\
重要模块介绍：
>1、writeCase.py ：自动读取新的Charles文件，并自动生成测试用例 \
 2、apiMethod.py：封装request方法，可以支持多协议扩展（get\post\put）\
 3、checkResult.py：封装验证response方法\
 4、setupMain.py： 核心代码，定义并执行用例集，生成报告\
 
![Aff_service.png](https://upload-images.jianshu.io/upload_images/7116457-f7858815cc858a31.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

----

详细介绍见原文:https://www.jianshu.com/p/6f5bfc1182ae
