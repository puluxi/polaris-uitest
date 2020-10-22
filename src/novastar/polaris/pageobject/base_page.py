import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    # 初始化driver
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            raise e
    # 获取单个页面元素
    def findElement(self, loc):
        try:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(loc))
            return element
        except Exception as e:
            raise e

    # 获取一组页面元素
    def findElements(self, loc):
        try:
            elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(loc))
            return elements
        except Exception as e:
            raise e

    # 最大化窗孔
    def maxWindow(self):
        try:
            self.driver.maximize_window()
        except Exception as e:
            raise e

    # 关闭窗口
    def closeWindow(self):
        try:
            self.driver.quit()
        except Exception as e:
            raise e

    # 点击操作
    def click(self, loc):
        try:
            self.findElement(loc).click
        except Exception as e:
            raise e

    #   设置值
    def sendKey(self, loc, key):
        try:
            self.findElement(loc).send_keys(Keys.CONTROL, 'a')
            self.findElement(loc).send_keys(key)
        except Exception as e:
            raise e
