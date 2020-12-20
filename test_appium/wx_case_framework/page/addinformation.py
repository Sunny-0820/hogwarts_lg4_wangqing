import yaml


from test_appium.wx_case_framework.page.base_page import BasePage, FileError


class AddInformation(BasePage):
    def add(self, name, gender, phone_number):
        self.name_param = name
        self.gender_param = gender
        self.phone_param = phone_number

        with open(self._filepath, encoding="utf-8") as f:
            file_content: dict = yaml.safe_load(f)
            if "addinformation" in file_content.keys():
                path = file_content["addinformation"]

                self.step(path)

            else:
                raise FileError(self._filepath)

        #局部导入
        from test_appium.wx_case_framework.page.addmembers import AddMembers
        return AddMembers(self._filepath, self._driver)