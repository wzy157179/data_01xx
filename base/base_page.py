"""
PO文件基类
"""
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_func(self, location, timeout=5, poll=.5):
        """
        元素定位方法
        :param location: 定位信息
        :param timeout: 超时时长
        :param poll: 方法执行间隔
        :return: 元素对象
        """
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(location[0], location[1]))
        return element

    def click_func(self, location):
        """元素点击方法"""
        element = self.find_element_func(location)  # 定位目标元素
        element.click()  # 调用点击方法

    def input_func(self, location, text):
        """元素输入方法"""
        element = self.find_element_func(location)  # 定位目标元素
        element.clear()  # 调用清空方法
        element.send_keys(text)  # 调用输入方法
