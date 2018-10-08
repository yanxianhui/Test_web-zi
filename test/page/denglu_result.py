from selenium.webdriver.common.by import By
from test.page.denglu import ERPdenglu
import  time
import os
class ERPDENGLU(ERPdenglu):
    loc_search_result = (By.XPATH, '//div[@class="header"]/span')
    #loc_search_result = (By.CSS_SELECTOR, '//p[@class="el-message__content"]')
    loc_search_sousuo = (By.XPATH, '//div/ul[1]/li[12]')
    loc_search_shuru = (By.XPATH, '//input[@placeholder="请输入搜索内容"]')
    loc_search_click = (By.XPATH, '//span[contains(text(),"搜索")]')
    loc_search_jianyan = (By.XPATH, '//tbody//td[1]/div[1]')
    loc_search_jieguo=(By.CSS_SELECTOR,'.el-message--error .el-message__content')

    loc_search_clickshoufahuo=(By.CSS_SELECTOR,'li.el-submenu:nth-child(2) > div:nth-child(1)')
    loc_search_clickshouHuo=(By.CSS_SELECTOR,'li.el-submenu:nth-child(2) > ul:nth-child(2) > li:nth-child(1)')
    loc_search_shouhuoshuru=(By.XPATH,'//input[@placeholder="输入搜索内容"]')
    loc_search_click_shousuo=(By.XPATH,'//span[contains(text(),"搜索")]')
    loc_search_click_bingli=(By.XPATH,'//tbody//td[1]')
    loc_search_click_shanghe=(By.CSS_SELECTOR,'.model_list > li:nth-child(1) > label:nth-child(2)')
    loc_search_click_xiahe=(By.CSS_SELECTOR,'.model_list > li:nth-child(1) > label:nth-child(3)')
    loc_search_shukuaididanhao=(By.CSS_SELECTOR,'.model_list > li:nth-child(1) > input:nth-child(5)')
    loc_search_click_tupianone=(By.CSS_SELECTOR,'.img_list > li:nth-child(1) > div:nth-child(2) > div:nth-child(1) > img:nth-child(1)')
    loc_search_click_tupiantwo=(By.CSS_SELECTOR,'.img_list > li:nth-child(2) > div:nth-child(2) > div:nth-child(1) > img:nth-child(1)')
    loc_search_click_querenshousuo=(By.XPATH,'//span[contains(text(),"确认收货")]')
    loc_search_click_fnagansheji=(By.CSS_SELECTOR,'li.el-submenu:nth-child(3)')
    loc_search_click_moxingshaomiao=(By.CSS_SELECTOR,'li.el-submenu:nth-child(3) > ul:nth-child(2) > li:nth-child(1)')
    loc_search_click_moxingshaomiao_shu=(By.XPATH,'//input[@placeholder="请输入搜索内容"]')
    loc_search_click_moxingshaomiao_sou=(By.XPATH,'//span[contains(text(),"搜索")]')
    loc_search_click_moxingshaomiao_annu=(By.XPATH,'//div[@id="tab-3"]')
    loc_search_click_moxingshaomiao_hege=(By.CSS_SELECTOR,'label.el-radio:nth-child(2) > span:nth-child(1) > span:nth-child(1)')
    loc_search_click_moxingshaomiao_quren=(By.CSS_SELECTOR,'button.block_btn:nth-child(3) > span:nth-child(1)')
    loc_search_click_moxingshaomiao_chuliwangc=(By.XPATH,'//span[contains(text(),"处理完成")]')
    #下面是病例成交xpath
    #loc_dianji_kefu=(By.CSS_SELECTOR,'li.el-submenu:nth-child(4) > div:nth-child(1)')
    loc_dianji_kefu=(By.XPATH,'//div[@class="nav_box nav"]/ul/li[4]/div')  #点击客服
    loc_dianji_kefu_BlCJ=(By.XPATH,'//div[@class="nav_box nav"]/ul/li[4]/ul/li[1]')  #点击病例成交
    #loc_dianji_kefu_BlCJ=(By.CSS_SELECTOR,'li.is-active:nth-child(1)')
    loc_search_kefu_shuru=(By.XPATH,'//input[@placeholder="填写搜索内容"]')

    loc_search_kefu_gougtong=(By.XPATH,'//tbody/tr/td[8]')           #是否沟通
    loc_search_kefu_binglihao=(By.XPATH,'//tbody/tr/td[8]/div[contains(text(),"否")]/../../td[1]')  #查找病例号

    loc_huoqu_diyihang_binglihao=(By.XPATH,'//tbody/tr[3]/td[8]/div/../../td[1]')  #获取第三行病例号

    loc_xiadan_click=(By.XPATH,'//tbody/tr/td[10]/div/button[2]/span')     #点击下单
    loc_dianjigoutong=(By.XPATH,'//tbody/tr/td[10]/div/button[1]/span')  #病例成交点击沟通
    loc_gouxuan=(By.XPATH,'//div[@class="el-card content"]//div/label[1]/input[1]')     #勾选已经联系上，本次沟通有内容
    loc_wenbenshuru=(By.XPATH,'//textarea[@type="textarea"]')    #数据沟通内容文本框
    loc_goutongneirongtijiao=(By.XPATH,'//div[@class="el-card content"]//div/button[2]')   #沟通有内容提交

    @property
    def result(self):
          return  self.find_elements(*self.loc_search_result)

    def sousuo(self, binglihao):
        self.find_element(*self.loc_search_sousuo).click()
        time.sleep(2)
        self.find_element(*self.loc_search_shuru).clear()
        self.find_element(*self.loc_search_shuru).send_keys(binglihao)
        self.find_element(*self.loc_search_click).click()

    def jianyan(self):
        return self.find_elements(*self.loc_search_jianyan)
    def jieguo(self):
        return  self.find_elements(*self.loc_search_jieguo)
    def jinrushousuo(self):
         self.find_element(*self.loc_search_clickshoufahuo).click()
         self.find_element(*self.loc_search_clickshouHuo).click()
    def shouhuosousuo(self,binglihao):
         self.find_element(*self.loc_search_shouhuoshuru).send_keys(binglihao)
         self.find_element(*self.loc_search_click_shousuo).click()
    def dainjibingli(self):
        self.find_element(*self.loc_search_click_bingli).click()
    def shoujianneirong(self):
        self.find_element(*self.loc_search_click_shanghe).click()
        self.find_element(*self.loc_search_click_xiahe).click()
        self.find_element(*self.loc_search_shukuaididanhao).send_keys('123456')
        self.find_element(*self.loc_search_click_tupianone).click()
        os.system("D:\\Ggshang1.exe")
        self.find_element(*self.loc_search_click_tupiantwo).click()
        os.system("D:\\Ggshang.exe")
        time.sleep(2)
        self.find_element(*self.loc_search_click_querenshousuo).click()

    def moxingshaomiao(self):
        self.find_element(*self.loc_search_click_fnagansheji).click()
        self.find_element(*self.loc_search_click_moxingshaomiao).click()
        time.sleep(1)
    def moxingshaomiaosuo(self,binglihao):
        self.find_element(*self.loc_search_click_moxingshaomiao_shu).send_keys(binglihao)
        self.find_element(*self.loc_search_click_moxingshaomiao_sou).click()
        time.sleep(1)
    def moxingzhijian(self):
        self.find_element(*self.loc_search_click_moxingshaomiao_annu).click()
        time.sleep(1)
    def zhijianhege(self):
        self.find_element(*self.loc_search_click_moxingshaomiao_hege).click()
        self.find_element(*self.loc_search_click_moxingshaomiao_quren).click()
        time.sleep(1)
    def chuliwangc(self):
        self.find_element(*self.loc_search_click_moxingshaomiao_chuliwangc).click()
        self.find_element(*self.loc_search_click_moxingshaomiao_shu).clear()
        time.sleep(1)
    def dianjikefu(self):
        self.find_element(*self.loc_dianji_kefu).click()
    def dianji_BLCJ(self):
        self.find_element(*self.loc_dianji_kefu_BlCJ).click()
    def kefusousuo(self,binglihao):
        self.find_element(*self.loc_search_kefu_shuru).send_keys(binglihao)
        self.find_element(*self.loc_search_click_shousuo).click()
        time.sleep(1)
        #self.find_element(*self.loc_search_kefu_shuru).clear()
    def chazhaogongtong(self):                   #返回是否沟通文本
        return  self.find_elements(*self.loc_search_kefu_gougtong)
    def kefubinglihao(self):                #返回客服界面位沟通病例号
        return self.find_elements(*self.loc_search_kefu_binglihao)

    def FirstNumber(self):
        return self.find_element(*self.loc_huoqu_diyihang_binglihao)
    def Xiadan(self):
        self.find_element(*self.loc_xiadan_click).click()
    def dianjiGTshi(self):
        self.find_element(*self.loc_dianjigoutong).click()
        time.sleep(2)
        self.find_element(*self.loc_gouxuan).click()
        self.find_element(*self.loc_wenbenshuru).send_keys('你好，方案已出，请查看！')
        time.sleep(2)
        self.find_element(*self.loc_goutongneirongtijiao).click()










