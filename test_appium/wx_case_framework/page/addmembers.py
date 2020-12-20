import yaml


from test_appium.wx_case_framework.page.base_page import BasePage, FileError


class AddMembers(BasePage):
    def goto_addinformation(self):
        with open(self._filepath, encoding="utf-8") as f:
            file_content: dict = yaml.safe_load(f)
            if "addmembers" in file_content.keys():
                path = file_content["addmembers"]

                self.step(path)

            else:
                raise FileError(self._filepath)

        #局部导入
        from test_appium.wx_case_framework.page.addinformation import AddInformation
        return AddInformation(self._filepath, self._driver)

    # 获取【添加成功】的Toast
    def verify_toast(self):
        result = self.get_toast_text()
        return result