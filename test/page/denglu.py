from selenium.webdriver.common.by import By
from test.common.page import Page
import  time

class ERPdenglu(Page):
    loc_search_input_user = (By.XPATH, '//input[@type="text"]')
    loc_search_input_pwd = (By.XPATH, '//input[@type="password"]')
    loc_search_button = (By.XPATH, '//*[@id="login"]/div[2]/div[2]/button')
    loc_search_result=(By.CSS_SELECTOR,'//p[@class="el-message__content"]')
    loc_search_sousuo=(By.XPATH,'//div/ul[1]/li[12]')
    loc_search_shuru=(By.XPATH,'//input[@placeholder="请输入搜索内容"]')
    loc_search_click=(By.XPATH,'//span[contains(text(),"搜索")]')
    loc_search_jianyan=(By.XPATH,'//tbody//td[1]/div[1]')
    loc_search_jieguo = (By.CSS_SELECTOR, '.el-message--error .el-message__content')
    def input_user(self, user):
        """搜索功能"""
        self.find_element(*self.loc_search_input_user).send_keys(user)
    def input_pwd(self, pwd):
        """搜索功能"""
        self.find_element(*self.loc_search_input_pwd).send_keys(pwd)
        self.find_element(*self.loc_search_button).click()
    #def result(self):
      #  return  self.find_element(*self.loc_search_result)

    def jieguo(self):
        return self.find_elements(*self.loc_search_jieguo)

