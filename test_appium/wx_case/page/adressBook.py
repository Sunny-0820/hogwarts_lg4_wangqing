from appium.webdriver.common.mobileby import MobileBy

from test_appium.wx_case.page.addMembers import AddMembers
from test_appium.wx_case.page.basepage import BasePage



class AdressBook(BasePage):

    # 点击【添加成员】
    _text = "添加成员"
    def goto_addmembers(self):
        self.find_by_scroll(self._text).click()
        return AddMembers(self._driver)

    # 点击【搜索】
    _content = (MobileBy.ID, "com.tencent.wework:id/i6n")
    def goto_search(self):
        self.find(*self._content).click()
        #局部导入SearchMembers
        from test_appium.wx_case.page.searchmembers import SearchMembers
        return SearchMembers(self._driver)