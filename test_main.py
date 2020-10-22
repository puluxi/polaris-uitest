import pytest
import allure
import time
from selenium import  webdriver
class TestUserManagement:
    @allure.feature("用户管理")
    @allure.story("进入用户管理界面")
    @allure.testcase("http://jira.vnnox.net/browse/VPIMP-1125","用户管理测试用例001")
    @allure.issue("http://jira.vnnox.net/browse/VPIMP-1125","Defect ID:VPIMP-1125")
    @allure.description("流程性的用例用户管理")
    def test_user_management_001(self):
        '''
        流程性的用例，
        用例步骤：1.登陆， 2.点击权限管理 3.点击用户管理  4.进入用户管理页面
        '''
        with allure.step("step1：打开浏览器"):
            driver = webdriver.Chrome()
            driver.get("http://172.16.6.108/user/login")
            driver.save_screenshot("截图1")
            driver.maximize_window()
        with allure.step("step2：点击权限管理"):
            driver.find_element_by_id("login-form_username").send_keys("admin")
            driver.save_screenshot("截图1")
            driver.find_element_by_id("login-form_password").send_keys("yjg123456")
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(5)
            driver.find_element_by_xpath("//span[text()='权限管理']/..").click()
            time.sleep(5)
        with allure.step("step3：点击用户管理"):
            driver.find_element_by_xpath("//span[text()='用户管理']/../..").click()
            time.sleep(5)
            entrance_flag = driver.find_element_by_xpath("//input[@id='loginName']").text
            assert entrance_flag == "请输入请输入登录账号"


    def test_user_management_002(self):
        pass


# class TestRoleManagement:
#
#     def test_role_management_001(self):
#         pass
#
#
# class TestDeptManagement:
#     def test_dept_management_001(self):
#         pass
#
#
# class TestPostManagement:
#     def test_post_management_001(self):
#         pass
#
#
# class TestMenuManagement:
#     def test_menu_management_001(self):
#         pass
