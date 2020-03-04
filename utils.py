"""
驱动获取方法
"""
from appium import webdriver


def get_driver():
    """驱动对象获取方法"""
    # 获取驱动对象
    capabilities = {
        "platformName": "Android",  # 测试平台（Android、iOS）
        "platformVersion": "5.1",  # 测试系统版本
        "deviceName": "模拟器",  # 测试设备名称
        "appPackage": "com.android.contacts",  # 待测应用的包名
        "appActivity": ".activities.PeopleActivity",  # 待测应用的启动名
        # 输入中文设置
        "resetKeyboard": True,
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver


if __name__ == '__main__':
    get_driver()

# 这道题太难了 俺不会做