import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

#自定义异常：文件内容异常
class FileError(Exception):

    def __init__(self, file):
        self.__file = file

    def __str__(self):
        return "Error:指定的文件中不包含配置信息，请检查文件：%s!" % self.__file


class BasePage:

    _back_list = []
    name_param = ""
    gender_param = ""
    phone_param = ""

    def __init__(self, file_path, driver:WebDriver=None):
        self._driver = driver
        self._filepath = file_path


    def find(self, by, locator=None):
        try:
            element = self._driver.find_element(*by) if isinstance(by,tuple) else self._driver.find_element(by,locator)
            return element

        except Exception as e:
            for back in self._back_list:
                elements = self._driver.find_elements(*back)
                elements.click()
                return self.find(by, locator)


    def find_by_scroll(self, text):
        element = self._driver.find_element_by_android_uiautomator \
            (f'new UiScrollable(new UiSelector().scrollable(true).instance(0))\
            .scrollIntoView(new UiSelector().text("{text}").instance(0))')
        return element


    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)

        except Exception as e:
            for back in self._back_list:
                elements = self._driver.find_elements(*back)
                elements.click()
                return self.send(value, by, locator)


    #根据性别进行不同的选择
    def choose_gender(self, gender_value):
        by = (MobileBy.XPATH,f"//*[@text='{gender_value}']")
        self.find(*by).click()


    def step(self, path):
        with open(path, encoding="utf=8") as f:
            steps:list[dict] = yaml.safe_load(f)
            for step in steps:
                #定位元素
                if "by" in step.keys():
                    if step["by"] == "text":
                        element = self.find_by_scroll(step["locator"])
                    else:
                        element = self.find(step["by"], step["locator"])
                #定位元素后对元素进行操作（click、send）
                if "click" in step.keys():
                    element.click()
                if "send" in step.keys():
                    content:str = step["send"]
                    content = content.replace("{name}", self.name_param)
                    content = content.replace("{phone_number}", self.phone_param)
                    self.send(content, step["by"], step["locator"])
                if "gender" in step.keys():
                    sex:str = step["gender"]
                    sex = sex.replace("{gender}", self.gender_param)
                    self.choose_gender(sex)


    #获取toast的text属性值，并返回text值
    def get_toast_text(self):
        result = self._driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        return result

