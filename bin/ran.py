import unittest,os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from conf.path import WEBCASE_PATH,REPOR_TPATH
from lib.HTMLTestRunner import HTMLTestRunner
from lib.tool import Tool
from lib.send_mail import sendmail



class Main(object):
    def run(self):
        #清理目录下存在的图片
        Tool().clear_picture()
        #生成测试套件
        suit = unittest.TestSuite()
        #获取测试用例
        cases = unittest.defaultTestLoader.discover(WEBCASE_PATH,'*.py')
        #循环添加测试用例至测试套件
        for case in cases:
            suit.addTest(case)
        #测试报告
        report_name = os.path.join(REPOR_TPATH,'UI测试报告.html')
        f = open(report_name,'wb')
        #以报告模版运行用例
        runner = HTMLTestRunner(f,verbosity=1,title='测试报告',description='用例执行情况：')
        res = runner.run(suit)
        #将报告文件写入磁盘，并关闭文件
        f.flush()
        f.close()

        success = res.success_count
        failure = res.failure_count

        #发送报告邮件
        title = 'UI测试报告'
        msg = '''
        大家好：
            本次UI测试结果如下：
                通过用例：%s条。
                失败用例：%s条。
                详情信息请看附件【%s】
        '''%(success,failure,os.path.basename(report_name))

        # sendmail(title,msg,report_name)

if __name__ == '__main__':
    Main().run()