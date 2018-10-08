import  unittest
from utils.HTMLTestRunner import HTMLTestRunner
from test.case.test_denglu import TestBaiDu
from utils.config import Config, DRIVER_PATH, DATA_PATH,REPORT_PATH
import time
from utils.mail import Email

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBaiDu))
    #now=time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(time.time()))
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb+') as f:
          runner = HTMLTestRunner(f, verbosity=2, title='第一个html报告', description='修改html报告')
          runner.run(testsuite)
    e = Email(title='ERP测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='825651673@qq.com',
              server='smtp.126.com',
              sender='luckyanhui@126.com',
              password='yan986165220',
              path=report
              )
    e.send()
    """初始化Email

            :param title: 邮件标题，必填。
            :param message: 邮件正文，非必填。
            :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
            :param server: smtp服务器，必填。
            :param sender: 发件人，必填。
            :param password: 发件人密码，必填。
            :param receiver: 收件人，多收件人用“；”隔开，必填。
            """