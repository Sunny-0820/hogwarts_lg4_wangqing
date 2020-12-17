from appium.webdriver.common.mobileby import MobileBy

from test_appium.wx_case.page.basepage import BasePage


class AddInformation(BasePage):
    # 添加成员信息
    _content_list = [
        (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/em7']//*[@text='必填']"),
        (MobileBy.ID, "com.tencent.wework:id/elq"),
        (MobileBy.XPATH, "//*[@text='手机号']"),
        (MobileBy.XPATH, "//*[@text='保存']")
    ]
    def add_members(self, name, gender, phone_number):
        self.send(name, *self._content_list[0])

        self.find(*self._content_list[1]).click()
        self.get_gender(gender)

        self.send(phone_number, *self._content_list[2])
        self.find(*self._content_list[3]).click()

        """
            注意：
                当存在A导入B，B导入A时，此时需要进行局部导入，在需要用到时再进行导入，否则工具会报错；
        """
        # 局部导入AddMembers
        from test_appium.wx_case.page.addMembers import AddMembers
        return AddMembers(self._driver)