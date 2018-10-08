import time
import unittest
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from test.page.denglu_result import ERPdenglu, ERPDENGLU
class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器firefox
        self.page = ERPdenglu(browser_type='chrome').get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        #self.page.quit()
        self.page.close()
        print("关闭")

    # def test_fouxiandan(self):
    #     datas = ExcelReader(self.excel).data
    #     user = 15890158362
    #     pwd = 123456
    #     self.sub_setUp()
    #     self.page.input_user(user)
    #     time.sleep(1)
    #     self.page.input_pwd(pwd)
    #
    #     #time.sleep(2)
    #     self.page = ERPDENGLU(self.page)
    #     #time.sleep(2)
    #     self.page.dianjikefu()
    #     time.sleep(2)
    #     self.page.dianji_BLCJ()
    #     time.sleep(3)
    #     BLh = self.page.kefubinglihao()
    #     bingli=[]
    #     for blh in BLh:
    #         bingli.append(blh.text)
    #     self.page.kefusousuo(bingli[0])
    #     time.sleep(1)
    #     self.page.Xiadan()
    #     time.sleep(2)
    #     texst=self.page.jieguo()
    #     for link in texst:
    #         self.assertEqual(link.text,'该病例暂未沟通')
    #         if link.text=='该病例暂未沟通1':
    #             pass
    #         else:
    #             self.page.save_screen_shot()
    #     self.sub_tearDown()
    #
    # def test_Shouhuo(self):
    #     datas = ExcelReader(self.excel, sheet=1).data
    #     user = 15890158362
    #     pwd = 123456
    #     self.sub_setUp()
    #     self.page.input_user(user)
    #     time.sleep(1)
    #     self.page.input_pwd(pwd)
    #     time.sleep(2)
    #     for d in datas:
    #         with self.subTest(data=d):
    #             self.page = ERPDENGLU(self.page)
    #             self.page.jinrushousuo()
    #             time.sleep(2)
    #             Bingli = self.page.FirstNumber()
    #             Binglihao = Bingli.text
    #             self.page.shouhuosousuo(Binglihao)
    #             time.sleep(3)
    #             self.page.dainjibingli()
    #             time.sleep(2)
    #             self.page.shoujianneirong()
    #             # sousuo=self.page.jieguo()
    #             # for sh in sousuo:
    #             # self.assertEqual(sh.text,d['Shjieguo'])
    #             time.sleep(3)
    #             self.page.moxingshaomiao()
    #             time.sleep(2)
    #             self.page.moxingshaomiaosuo(Binglihao)
    #             time.sleep(3)
    #             self.page.dainjibingli()
    #             time.sleep(2)
    #             self.page.moxingzhijian()
    #             time.sleep(2)
    #             self.page.zhijianhege()
    #             # btjiao=self.page.jieguo()
    #             # for bt in btjiao:
    #             # self.assertEqual(d['Tbutton'],bt.text)
    #             time.sleep(3)
    #             self.page.chuliwangc()
    #             linkp = self.page.jieguo()
    #             # print(links.text)
    #             for linke in linkp:
    #                 logger.info(linke.text)
    #                 self.assertEqual(linke.text, '暂无数据')
    #         self.sub_tearDown()
    def test_search(self):
        datas = [[15890158362,123456,'登录成功'],[15890158362,'','请输入密码'],[15890158362,12456,'用户名或密码错误！']]
        for d in datas:
            with self.subTest(data=d):
                print(d[0])
                print(d[1])
                self.sub_setUp()
                self.page.input_user(d[0])
                time.sleep(1)
                self.page.input_pwd(d[1])
                time.sleep(2)
                # self.page.result()
                #self.page = ERPDENGLU(self.page)  # 页面跳转到result page
                links = self.page.jieguo()
                # print(links.text)
                for link in links:
                    logger.info(link.text)
                    self.assertEqual(link.text, d[2])
                self.sub_tearDown()

if __name__ == '__main__':
    # report = REPORT_PATH + '\\report.html'
    # with open(report, 'wb') as f:
    # runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
    #  runner.run(TestBaiDu('test_search'))

    # TestBaiDu('test_search')
    TestBaiDu('test_search')
    # e = Email(title='百度搜素测试报告',
    #           message='这是今天的测试报告，请查收！',
    #           receiver='396214358@qq.com',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    # e.send()
