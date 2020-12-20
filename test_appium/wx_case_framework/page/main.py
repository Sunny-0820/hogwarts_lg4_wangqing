import yaml

from test_appium.wx_case_framework.page.adressbook import AdressBook
from test_appium.wx_case_framework.page.base_page import BasePage, FileError


class Main(BasePage):
    def goto_adressbook(self):
        with open(self._filepath, encoding="utf-8") as f:
            file_content :dict = yaml.safe_load(f)
            if "main" in file_content.keys():
                path = file_content["main"]

                self.step(path)

            else:
                raise FileError(self._filepath)

        return AdressBook(self._filepath, self._driver)