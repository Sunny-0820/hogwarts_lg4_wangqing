import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:

    logging.basicConfig(level=logging.INFO)


    _back_list = [(MobileBy.XPATH, "//*[@class='android.widget.ImageView']")]
    _error_cont = 0
    _error_max = 10

    #设置日志
    # logging.basicConfig(level=logging.INFO,
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt='%a, %d %b %Y %H:%M:%S',
    #                     filename='../log/myapp.log',
    #                     filemode='w')


    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    #定义find函数进行元素查找，并进行异常处理（弹窗处理）
    def find(self, by, locator):
        try:
            # 日志打印
            logging.info("find:")
            # logging.info(by)
            # logging.info(locator)

            element1 = self._driver.find_element(by, locator)
            self._error_cont = 0
            return element1

        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for back in self._back_list:
                element2 = self._driver.find_element(*back)
                element2.click()
                return self.find(by, locator)

    #定义send函数进行输入框的数据输入，并进行异常处理（弹窗处理）
    def send(self, value, by, locator):
        try:
            self.find(by,locator).send_keys(value)
            self._error_cont = 0

        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for back in self._back_list:
                element3 = self._driver.find_element(*back)
                element3.click()
                return self.send(value, by, locator)

    #滚动查找
    def find_by_scroll(self, text):

        #日志打印
        # logging.info("find_by_scroll:")
        # logging.info(text)

        element = self._driver.find_element_by_android_uiautomator \
            (f'new UiScrollable(new UiSelector().scrollable(true).instance(0))\
            .scrollIntoView(new UiSelector().text("{text}").instance(0))')
        return element

    #获取toast的text属性值，并返回text值
    def get_toast_text(self):
        result = self._driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

        #日志打印
        # logging.info("get_toast_text:")
        # logging.info(result)

        return result

    #获取性别
    def get_gender(self, gender):
        content = (MobileBy.XPATH, f"//*[@text='{gender}']")
        self.find(*content).click()

    def get_elements_number(self, by, locator):
        try:
            elements = self._driver.find_elements(by, locator)
            self._error_cont = 0
            return len(elements)

        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for back in self._back_list:
                element2 = self._driver.find_element(*back)
                element2.click()
                return self.find(by, locator)
