import driver as driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  random
import time

from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Chrome()
driver.get("http://172.16.6.108/user/login")
driver.maximize_window()
driver.find_element_by_id("login-form_username").send_keys("admin")
driver.find_element_by_id("login-form_password").send_keys("yjg123456")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='权限管理']/..").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='用户管理']/../..").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='ant-card ant-card-middle']//button[@class='ant-btn ant-btn-primary']").click()
time.sleep(5)
usernameNO = str(random.randint(0,10000))
loginnameNO = str(random.randint(0,10000))
phoneNO = str(random.randint(9999999,100000000))
username = "NovaAuto" + usernameNO
loginname = "NovaAuto" + loginnameNO
phonenumer = "187" + phoneNO

driver.find_element_by_id("userName").send_keys(username)
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']").send_keys(phonenumer)
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='请输入登录账号']").send_keys(loginname)
time.sleep(1)
driver.find_element_by_xpath("//input[@id='sex']").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@title='女']").click()
time.sleep(1)
driver.find_element_by_xpath("//span[text()='请选择岗位']/..").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@title='系统测试工程师']").click()
time.sleep(1)
driver.find_element_by_xpath("//span[text()='请选择归属部门']/../..").click()
time.sleep(1)
driver.find_element_by_xpath("//span[@title='视频测试组']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='password']").send_keys("888888")
driver.find_element_by_xpath("//span[text()='确 定']/..").click()
element =  driver.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr[1]/td[3]")
page_loginname = element.text
element  =  driver.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr[1]/td[4]")
page_username  = element.text
assert page_loginname == loginname
assert  page_username == username
