import time
import unittest
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from test.page.denglu_result import ERPdenglu,ERPDENGLU
import sys


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'
    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器firefox
        self.page = ERPdenglu(browser_type='chrome').get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        #self.page.save_screen_shot()
        #time.sleep(1)
        #self.page.quit()
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            self.page.save_screen_shot("Screenshots/%s.png" % test_method_name)
        time.sleep(2)
        super(TestBaiDu, self).tearDown()


    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.input_user(d['user'])
                time.sleep(1)
                self.page.input_pwd(d['pwd'])
                time.sleep(2)
                #self.page.result()
                self.page = ERPDENGLU(self.page)  # 页面跳转到result page
                links =self.page.jieguo()
                #print(links.text)
                for link in links:
                    logger.info(link.text)
                    self.assertEqual(link.text,d['result'] )
                self.sub_tearDown()




    def test_sousuo(self):
        datas = ExcelReader(self.excel).data
        user = 15890158362
        pwd = 123456
        self.sub_setUp()
        self.page.input_user(user)
        time.sleep(1)
        self.page.input_pwd(pwd)
        time.sleep(2)
        for d in datas:
            with self.subTest(data=d):
                self.page = ERPDENGLU(self.page)
                self.page.sousuo(d['bingli'])
                time.sleep(2)
                lings=self.page.jianyan()
                for link in lings:
                    print(lings)
                self.assertEqual(link.text,d['bingli'])
        self.sub_tearDown()
       


    ''' 
    def test_Shouhuo(self):
        datas = ExcelReader(self.excel, sheet=1).data
        user = 15890158362
        pwd = 123456
        self.sub_setUp()
        self.page.input_user(user)
        time.sleep(1)
        self.page.input_pwd(pwd)
        time.sleep(2)
        for d in datas:
            with self.subTest(data=d):
                self.page = ERPDENGLU(self.page)
                self.page.jinrushousuo()
                time.sleep(2)
                Bingli=self.page.FirstNumber()
                Binglihao=Bingli.text
                self.page.shouhuosousuo(Binglihao)
                time.sleep(3)
                self.page.dainjibingli()
                time.sleep(2)
                self.page.shoujianneirong()
                # sousuo=self.page.jieguo()
                # for sh in sousuo:
                # self.assertEqual(sh.text,d['Shjieguo'])
                time.sleep(3)
                self.page.moxingshaomiao()
                time.sleep(2)
                self.page.moxingshaomiaosuo(Binglihao)
                time.sleep(3)
                self.page.dainjibingli()
                time.sleep(2)
                self.page.moxingzhijian()
                time.sleep(2)
                self.page.zhijianhege()
                # btjiao=self.page.jieguo()
                # for bt in btjiao:
                # self.assertEqual(d['Tbutton'],bt.text)
                time.sleep(2)
                self.page.chuliwangc()
                linkp = self.page.jieguo()
                # print(links.text)
                for linke in linkp:
                    logger.info(linke.text)
                self.assertEqual(linke.text,'暂无数据')
            self.sub_tearDown()
               '''


    def test_fouxiandan(self):
        datas = ExcelReader(self.excel).data
        user = 15890158362
        pwd = 123456
        self.sub_setUp()
        self.page.input_user(user)
        time.sleep(1)
        self.page.input_pwd(pwd)
        time.sleep(2)
        self.page = ERPDENGLU(self.page)
        time.sleep(2)
        self.page.dianjikefu()
        time.sleep(2)
        self.page.dianji_BLCJ()
        time.sleep(3)
        BLh = self.page.kefubinglihao()
        bingli=[]
        for blh in BLh:
            bingli.append(blh.text)
        self.page.kefusousuo(bingli[1])
        time.sleep(1)
        self.page.Xiadan()
        time.sleep(2)
        texst=self.page.jieguo()
        for link in texst:
            self.assertEqual(link.text,'该病例暂未沟通')
        self.sub_tearDown()




    def test_goutong_jianyanshi(self):
        user = 15890158362
        pwd = 123456
        self.sub_setUp()
        self.page.input_user(user)
        time.sleep(1)
        self.page.input_pwd(pwd)
        time.sleep(2)
        self.page = ERPDENGLU(self.page)
        time.sleep(2)
        self.page.dianjikefu()
        time.sleep(2)
        self.page.dianji_BLCJ()
        time.sleep(3)
        BLh = self.page.kefubinglihao()
        bingli=[]
        for blh in BLh:
            bingli.append(blh.text)
        self.page.kefusousuo(bingli[1])
        time.sleep(1)
        self.page.dianjiGTshi()
        time.sleep(2)
        texst=self.page.chazhaogongtong()
        for link in texst:
            self.assertEqual(link.text,'是')
        self.sub_tearDown()
if __name__ == '__main__':
    #report = REPORT_PATH + '\\report.html'
   # with open(report, 'wb') as f:
       # runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
      #  runner.run(TestBaiDu('test_search'))

    #TestBaiDu('test_search')
    TestBaiDu('test_goutong_jianyanshi')
    # e = Email(title='百度搜素测试报告',
    #           message='这是今天的测试报告，请查收！',
    #           receiver='396214358@qq.com',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    # e.send()
