'''
描述：
编写人：
实现步骤：
    1.加载测试用例
    2.运行用例并生成报告
    3.发送测试报告邮件
'''
import os.path
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.congfigEmail import configEmail


def createTestSuit():
    case_dir = os.path.dirname(__file__) + '/testCase'
    print('case_dir=', case_dir)
    suite = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='Test*.py')
    # print(suite)
    return suite


if __name__ == '__main__':
    case_suite = createTestSuit()
    sendtime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    filename = os.path.dirname(__file__) + '/report/' + sendtime + ' report.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title='自动化测试用例报告', description='测试用例执行情况')
        runner.run(case_suite)

    report_dir = os.path.dirname(__file__) + '/report/report.html'
    ce = configEmail()
    ce.sendAttachEmail(report_dir)