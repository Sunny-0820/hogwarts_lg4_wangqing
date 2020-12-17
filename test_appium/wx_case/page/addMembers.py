from appium.webdriver.common.mobileby import MobileBy

from test_appium.wx_case.page.basepage import BasePage


class AddMembers(BasePage):
    # 点击【手动输入添加】
    _content = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    def goto_addinformation(self):
        self.find(*self._content).click()
        """
            注意：
                当存在A导入B，B导入A时，此时需要进行局部导入，在需要用到时再进行导入，否则工具会报错；
        """
        # 局部导入AddInformation
        from test_appium.wx_case.page.addInformation import AddInformation
        return AddInformation(self._driver)

    # 获取【添加成功】的Toast
    def verify_toast(self):
        result = self.get_toast_text()
        return result