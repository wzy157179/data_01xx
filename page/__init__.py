from selenium.webdriver.common.by import By

# 通讯录列表页面
new_item = By.ID, 'com.android.contacts:id/floating_action_button'  # 新建联系人按钮

# 新建联系人页面
local_btn = By.ID, 'com.android.contacts:id/left_button'  # 本地保存按钮
name = By.XPATH, '//*[@text="姓名"]'  # 姓名
phone = By.XPATH, '//*[@text="电话"]'  # 电话
