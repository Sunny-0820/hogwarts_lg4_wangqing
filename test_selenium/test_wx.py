"""
    企业微信的添加成员模块测试
    https://work.weixin.qq.com/wework_admin/frame
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):

        # 复用浏览器
            # 注意：9222 端口要与命令行启动的端口保持一致 --remote-debugging-port=9222
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_arg)

        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(5)


    def test_wx(self):

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        #get_cookies()得到浏览器所有cookies
        #print(self.driver.get_cookies())
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '304547759805351'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604851140, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '120rste'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1667820771, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1369060082.1604731054'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607411607, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1604835171, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.59377991.1604731054'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636283919, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604731053'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636267045, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}
        ]

        #for循环将所有cookies通过add_cookie()加入到浏览器中
        for cookie in cookies:
            self.driver.add_cookie(cookie)


        #刷新浏览器
        self.driver.refresh()
        phone_number = "12345678901"
        self.driver.find_element_by_xpath('//div[@class="index_service_cnt js_service_list"]/a[1]').click()
        self.driver.find_element_by_id("username").send_keys("aa1")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("a_1")
        self.driver.find_element_by_id("memberAdd_phone").send_keys(phone_number)
        self.driver.find_element_by_link_text("保存").click()
        sleep(3)

        #检查人员是否添加完成

        #人员添加完成后检查是否添加成功
        result = self.driver.find_element(By.XPATH, '//*[@id="member_list"]/tr[1]/td[5]')
        assert  result.text == phone_number
        #print(result)