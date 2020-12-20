import pytest
import yaml

from test_appium.wx_case_framework.page.app import App


class TestAdd:

    def setup_class(self):
        wx_file_path = "wx.yaml"
        self.app = App(wx_file_path)

    def setup(self):
        self.main = self.app.start().main()

    def teardown_class(self):
        self.app.stop()

    file_content = yaml.safe_load(open("data.yaml", encoding="UTF-8"))
    @pytest.mark.parametrize("name,gender,phone_number", file_content["members"])
    def test_add(self, name, gender, phone_number):
        result = self.main.goto_adressbook().goto_addmembers()\
            .goto_addinformation().add(name, gender, phone_number).get_toast_text()
        assert result == "添加成功"

