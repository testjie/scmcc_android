### scmcc_android
    基于appium-python的安卓app自动化测试框架

#### 1. 项目简介

#### 2. 环境配置

#### 3. 如何使用

#### 4. 持续优化
    1. 测试结果报告截图
    2. 自动发送邮件
    3. 扩展关键字驱动

#### 5. 问题
    1. 禁止appium重复安装Unlock、Setting、Android Input Manager等apk，防止第三方rom出现弹窗提示的问题
    
    step1:
    ~\Appium\resources\app\node_modules\appium\node_modules\appium-android-driver\lib\android-helpers.js
    搜索并注释:
    await adb.install(unicodeIMEPath, {replace: false})
    await helpers.pushSettingsApp(adb)
    await helpers.pushUnlock(adb)
    
    step2:
    \Appium\resources\app\node_modules\appium\node_modules\appium-android-driver\build\lib\android-helpers.js
    a. 
    注释这行：
    return _regeneratorRuntime.awrap(adb.install(_appiumAndroidIme.path, { replace: false }));
    替换成这行：
    return context$1$0.abrupt('return', false)
    
    b. 
    注释这行：
    return _regeneratorRuntime.awrap(helpers.pushSettingsApp(adb))
    替换成这行：
    return context$1$0.abrupt('return', false)
    
    c. 
    注释这行：
    return _regeneratorRuntime.awrap(helpers.pushUnlock(adb));
    替换成这行：
    return context$1$0.abrupt('return', false)

    2. driver.close() 出现报错，待解决
    selenium.common.exceptions.WebDriverException: Message: Method has not yet been implemented