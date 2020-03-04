"""
新建联系人页面
"""
import page
from base.base_page import BasePage


class NewItemPage(BasePage):
    new_item = page.new_item  # 新建联系人按钮

    def click_new_item(self):
        """点击新建联系人按钮"""
        self.click_func(self.new_item)
