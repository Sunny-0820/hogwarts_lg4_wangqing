from appium import webdriver

from test_appium.wx_case.page.basepage import BasePage
from test_appium.wx_case.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.tencent.wework"
        _activity = ".launch.LaunchSplashActivity"
        if self._driver == None:
            print("self._driver is None")
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "device"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["noReset"] = "true"
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self._driver.quit()

    def goto_main(self):
        return Main(self._driver)