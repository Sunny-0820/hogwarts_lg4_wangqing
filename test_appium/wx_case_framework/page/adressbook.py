import yaml

from test_appium.wx_case_framework.page.addmembers import AddMembers
from test_appium.wx_case_framework.page.base_page import BasePage, FileError


class AdressBook(BasePage):
    def goto_addmembers(self):
        with open(self._filepath, encoding="utf-8") as f:
            file_content: dict = yaml.safe_load(f)
            if "adressbook" in file_content.keys():
                path = file_content["adressbook"]

                self.step(path)

            else:
                raise FileError(self._filepath)

        return AddMembers(self._filepath, self._driver)