import pytest
import allure
import time
from selenium import  webdriver
from src.novastar.polaris.pageobject.user_page import UserPage
class TestUserManagement:
    @allure.feature("用户管理")
    @allure.story("进入用户管理界面")
    @allure.testcase("http://jira.vnnox.net/browse/VPIMP-1125","用户管理测试用例001")
    @allure.issue("http://jira.vnnox.net/browse/VPIMP-1125","Defect ID:VPIMP-1125")
    @allure.description("流程性的用例用户管理")
    def test_user_management_001(self):
        pass


    def test_user_management_002(self):
        pass


class TestRoleManagement:

    def test_role_management_001(self):
        pass


class TestDeptManagement:
    def test_dept_management_001(self):
        pass


class TestPostManagement:
    def test_post_management_001(self):
        pass


class TestMenuManagement:
    def test_menu_management_001(self):
        pass
