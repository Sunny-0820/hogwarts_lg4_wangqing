from appium.webdriver.common.mobileby import MobileBy

from test_appium.wx_case.page.basepage import BasePage
from test_appium.wx_case.page.personalinformation import PersonalInformation


class SearchMembers(BasePage):
    def goto_personalinformation(self,name):
        content_list = [
            (MobileBy.XPATH, "//*[@text='搜索']"),
            (MobileBy.ID, "com.tencent.wework:id/e6d"),
            (MobileBy.XPATH, f"//*[@resource-id='com.tencent.wework:id/gqx']//*[@text='{name}']")
        ]
        self.send(name, *content_list[0])
        element1 = self.get_elements_number(*content_list[1])

        self.find(*content_list[2]).click()

        return PersonalInformation(self._driver), element1


    def verify_delete_number(self):
        content = (MobileBy.ID, "com.tencent.wework:id/e6d")
        element2 = self.get_elements_number(*content)
        return element2