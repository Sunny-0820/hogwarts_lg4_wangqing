from time import sleep

from appium import webdriver

"""
    删除微信联系人测试用例
    用find_elements获取元素列表
"""
class TestWX:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "device"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_deletenumber(self):

        name = "hogwarts_003"

        # 点击通讯录
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()

        # 点击搜索
        self.driver.find_element_by_id("com.tencent.wework:id/i6n").click()

        #在搜索框查找联系人
        self.driver.find_element_by_xpath("//*[@text='搜索']").send_keys(name)

        #删除联系人
        element1 = self.driver.find_elements_by_id("com.tencent.wework:id/e6d")
        element1[0].click()

        self.driver.find_element_by_id("com.tencent.wework:id/i6d").click()
        self.driver.find_element_by_xpath("//*[@text='编辑成员']").click()

        self.driver.find_element_by_android_uiautomator \
                ('new UiScrollable(new UiSelector().scrollable(true).instance(0))\
                .scrollIntoView(new UiSelector().text("删除成员").instance(0))').click()

        self.driver.find_element_by_id("com.tencent.wework:id/blx").click()
        sleep(2)

        # 判断是否删除成功
        element2 = self.driver.find_elements_by_id("com.tencent.wework:id/e6d")
        assert len(element2) + 1 == len(element1)
