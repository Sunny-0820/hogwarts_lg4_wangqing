from appium.webdriver.common.mobileby import MobileBy

from test_appium.wx_case.page.basepage import BasePage



class EditInformation(BasePage):
    _text = "删除成员"
    _content = (MobileBy.ID, "com.tencent.wework:id/blx")
    def delete_members(self):
        self.find_by_scroll(self._text).click()
        self.find(*self._content).click()
        #局部导入SearchMembers
        from test_appium.wx_case.page.searchmembers import SearchMembers
        return SearchMembers(self._driver)