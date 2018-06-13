**基于selenuim2的web自动化测试框架**
    
     由于公司经常出现ECP分割、BOSS系统维护，而这些操作可能会对现有系统造成不可预估的风险，
     需要大量测试人员手动巡检，为了减轻测试人员的压力，所以开发这个轻量级的web自动化测试框架。
                                                                 - SNake
1.项目简介

    1. 基于python脚本编写，不需要借助其他工具，环境配置简单。
    2. 采用数据驱动的方式，后期只需按照固定格式维护xml数据，脚本维护少。
    3. 测试环境依赖只需要见到命令即可，依赖极少 。
    4. 采用po分层实现用例和数据的隔离，后期只需专注于case和data设计，无需其他代码维护。
    5. 测试结果后自动生成html单文件测试报告，统计测试执行情况，执行情况详细，配合自动截图，
       可快速定位问题，并且容易扩展优化。

2.环境依赖和运行入口

    依赖：
        pip3 install -r requirements.txt
    运行：
        1. 设置config.py中PRO_ROOT_PATH为当前目录的根目录
        2. python run.py


3.项目结构

    scmcc_web:
        |---- config层                   配置层，放项目配置文件
        |---- data层                     数据层，放数据文件，把testcase参数化的文件放到这里，一般用xml、excel，好处是把数据与代码隔离开，数据驱动测试原则）
        |---- drivers层                  驱动层，放selenium2所需驱动，如ChromeDriver、FirefoxDrider等
        |---- log层                      日志层，放执行日志文件，如xxx.log等（暂未启用）
        |---- report层                   报告层，放测试执行报告，后期自动发送Email功能所需文件的目录
        |---- scr层                      代码层，各种执行代码
        |       |---- test                      测试代码层
        |       |       |---- case              测试用例
        |       |       |---- common            测试共用方法
        |       |       |---- page              po层，放页面对象，便于维护页面元素
        |       |       |---- suite             测试集合，用于组织测试用例
        |       |---- utils                     工具层，存放各种工具代码
        |---- venv层                     环境层，放windows环境下的虚拟环境
        |---- ReadMe.md                  项目介绍文件，可以用于项目介绍和后期项目功能备注
        |---- requirements.txt           项目依赖文件，使用pip3 install -r requirements.txt
        |---- run.py                     项目执行入口


4.执行流程
    
    1. runner -> testsuites -> testcase -> page -> runcase -> htmltestrunner自动执行失败case和收集收集截图
    2  自动执行src.test.case中test_开头的case集合
    3. page中创建并保存各个页面的元素对象,重构各个操作的业务流代码
        其中，__init__：识别并保存页面对象，须将selenium对象命名为sele.driver即可。
    4. testcase中调用具体的业务流函数就OK了
    5. 数据驱动，利用ddt框架实现，具体见test1_search
    6. 业务流测试，无须做参数化


5.后期优化

    1. 增加日志功能，测试每一个步骤记录日志
    2. 增加email模块，实现自动发送测试结果到指定邮箱功能
    3. 优化xml数据存放格式，增加数据可读性
    

6.参考

    1. htmltestrunner参考： https://github.com/GoverSky/HTMLTestRunner/