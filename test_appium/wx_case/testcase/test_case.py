from test_appium.wx_case.page.app import App


class TestCase:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    # 企业微信添加联系人测试用例
    def test_add(self):
        name = "hogwarts_9"
        gender = "女"
        phone_number = "12345678909"
        result = self.main.goto_adressbook().goto_addmembers().goto_addinformation().add_members(name, gender, phone_number).verify_toast()
        assert result == "添加成功"


    # 企业微信删除联系人测试用例
    def test_delete(self):
        name = "hogwarts_9"
        page, element1 = self.main.goto_adressbook().goto_search().goto_personalinformation(name)
        element2 = page.goto_information().goto_editpersonal().delete_members().verify_delete_number()
        assert element1 - element2 == 1

    def teardown_class(self):
        self.app.stop()