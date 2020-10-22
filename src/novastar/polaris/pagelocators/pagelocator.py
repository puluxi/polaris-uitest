from selenium.webdriver.common.by import By

# Login Page 登录页面
LOGIN_UNAME = (By.ID, "login-form_username")
LOGIN_PASSWD = (By.ID, "login-form_password")
LOGIN_SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")

# AuthorityManagement Page 权限管理页面
NAVIGATE_BAR_AUTH = (By.XPATH, "//span[text()='权限管理']/..")
NAVIGATE_BAR_USER = (By.XPATH, "//span[text()='用户管理']/../..")

# UserManagement Page 用户管理页面
#***************************************添加用户的页面元素 *****************************
USER_PAGE_ADD_BTN = (By.XPATH, "//div[@class='ant-card ant-card-middle']//button[@class='ant-btn ant-btn-primary']")
USER_PAGE_UNAME =  (By.ID, "userName")
USER_PAGE_PHONE =  (By.XPATH, "//input[@placeholder='请输入手机号码']")
USER_PAGE_LOGINANAME =  (By.XPATH, "//input[@placeholder='请输入登录账号']")
USER_PAGE_SEX =  (By.XPATH, "//input[@id='sex']")
USER_PAGE_SEX_VALUE =  (By.XPATH, "//div[@title='女']")
USER_PAGE_POST =  (By.XPATH, "//span[text()='请选择岗位']/..")
USER_PAGE_POST_VALUE =  (By.XPATH, "//div[@title='系统测试工程师']")
USER_PAGE_DEPT =  (By.XPATH, "//span[text()='请选择归属部门']/../..")
USER_PAGE_DEPT_VALUE =  (By.XPATH, "//span[@title='视频测试组']")
USER_PAGE_PASSWD =  (By.XPATH, "//input[@id='password']")
USER_PAGE_OK =  (By.XPATH, "//span[text()='确 定']/..")
#*************************************** end******************************************
#***************************************用户查询页面元素*****************************
USER_RESULT_LOGINANAME = (By.XPATH, "//tbody[@class='ant-table-tbody']/tr[1]/td[3]")
USER_RESULT_UNAME = (By.XPATH, "//tbody[@class='ant-table-tbody']/tr[1]/td[4]")
#*************************************** end******************************************

# RoleManagement Page 角色管理页面

# DeptManagement Page 部门管理页面

# PostManagement Page 岗位办理页面

# MenuManagement Page 菜单管理页面

