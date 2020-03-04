"""
通讯录列表页面
"""
import page
from base.base_page import BasePage


class AddressListPage(BasePage):
    local_btn = page.local_btn  # 本地保存
    name = page.name  # 姓名
    phone = page.phone  # 电话

    def click_local_btn(self):
        """点击本地保存按钮"""
        self.click_func(self.local_btn)

    def input_name(self, name):
        """输入姓名"""
        self.input_func(self.name, name)

    def input_phone(self, phone):
        """输入电话"""
        self.input_func(self.phone, phone)
