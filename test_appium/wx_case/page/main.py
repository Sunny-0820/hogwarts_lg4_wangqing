from appium.webdriver.common.mobileby import MobileBy

from test_appium.wx_case.page.adressBook import AdressBook
from test_appium.wx_case.page.basepage import BasePage


class Main(BasePage):
    # 点击【通讯录】
    _content = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_adressbook(self):
        self.find(*self._content).click()
        return AdressBook(self._driver)