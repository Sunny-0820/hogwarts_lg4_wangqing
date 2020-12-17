from appium.webdriver.common.mobileby import MobileBy

from test_appium.wx_case.page.basepage import BasePage
from test_appium.wx_case.page.editinformation import EditInformation


class Information(BasePage):
    _content = (MobileBy.XPATH, "//*[@text='编辑成员']")
    def goto_editpersonal(self):
        self.find(*self._content).click()
        return EditInformation(self._driver)