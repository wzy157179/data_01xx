"""
通讯录测试用例
"""
import time
import pytest

from data.read_yaml import build_address_finc
from page.address_list_page import AddressListPage
from page.new_item_page import NewItemPage
from utils import get_driver


class TestAddress(object):
    """通讯录测试类"""

    @pytest.fixture(autouse=True)
    def before_func(self):
        self.drvier = get_driver()  # 获取驱动对象
        self.new_item_page = NewItemPage(self.drvier)  # 获取新建联系人页面对象
        self.address_list_page = AddressListPage(self.drvier)  # 获取通讯录列表页面对象
        yield  # 结束工作
        time.sleep(3)
        self.drvier.quit()

    @pytest.mark.parametrize('name,phone',build_address_finc())
    def test_address(self,name,phone):
        """通讯测试方法"""
        self.new_item_page.click_new_item()  # 点击新建联系人按钮
        self.address_list_page.click_local_btn()  # 点击本地保存
        self.address_list_page.input_name(name)  # 输入姓名
        self.address_list_page.input_phone(phone)  # 输入电话
        self.drvier.keyevent(4)  # 调用返回键,保存信息
