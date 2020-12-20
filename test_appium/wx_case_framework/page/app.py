import yaml
from appium import webdriver

from test_appium.wx_case_framework.page.base_page import BasePage, FileError
from test_appium.wx_case_framework.page.main import Main


class App(BasePage):
    """
    def start(self):
        _package = "com.tencent.wework"
        _activity = ".launch.LaunchSplashActivity"
        if self._driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "device"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["noReset"] = "true"
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)

        else:
            self._driver.start_activity(_package, _activity)

        #return self:链式调用,返回类的实例本身
        return self
    """

    def start(self):
        with open(self._filepath, encoding="utf-8") as f:
            file_content :dict = yaml.safe_load(f)
            if "App" in file_content.keys():
                path = file_content["App"]

                with open(path, encoding="utf-8") as f:
                    config: dict = yaml.safe_load(f)
                    if "caps" in config.keys():
                        config_caps = config["caps"]
                    if "url" in config.keys():
                        config_url = config["url"]

                if self._driver == None:
                    self._driver = webdriver.Remote(config_url, config_caps)
                    self._driver.implicitly_wait(5)
                else:
                    self._driver.launch_app()
                return self

            else:
                raise FileError(self._filepath)



    def stop(self):
        self._driver.quit()


    def main(self):
        return Main(self._filepath, self._driver)

