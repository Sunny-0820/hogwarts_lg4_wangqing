from appium.webdriver.common.mobileby import MobileBy

from test_appium.wx_case.page.basepage import BasePage
from test_appium.wx_case.page.information import Information


class PersonalInformation(BasePage):
    _content = (MobileBy.ID, "com.tencent.wework:id/i6d")
    def goto_information(self):
        self.find(*self._content).click()
        return Information(self._driver)