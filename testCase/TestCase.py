'''
功能描述：调用readExcel模块，读取测试数据，根据不同的请求方式，进行接口请求
编写人：chenyanna
实现步骤：
    1.实例化调用readExcel模块，读取测试数据
    2.根据测试数据中的每个接口的请求method决定进行对应的请求
        2-1 get，调用request.get()
            2-1-1 准备接口请求的所有参数
                1-url
                2-params
                3-header（cookie）
                4.timeout
        2-2 post,调用request。post()
            2-2-1 准备接口请求的所有参数
                1-url
                2-data(json)
                3-header（cookie）
                4.timeout
    3.获取每个接口的响应结果实际结果，与表中的预期进行断言

'''

from unittest import TestCase

from ddt import ddt,data,unpack
import requests as requests

from common.configHttp import ConfigHttp
from common.readExcel import ReadExcel
import unittest

re = ReadExcel()
case_data = re.read()

@ddt
class TestCaseClass(unittest.TestCase):


    #1.初始化方法
    @classmethod
    def setUpClass(cls):
        pass
        # re = ReadExcel()
        # cls.case_data = re.read()
        # print(cls.case_data)



    def setUp(self):

        print('每条测试用例执行前执行')

    #2.测试方法
    '''
    [{'id': 1.0, 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'Method': 'post', 'value': "{'username':'zhuxiaodong','password':'test01'}", 'except': 0.0, 'real': '', 'status': ''}, 
    {'id': 2.0, 'interfaceUrl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'Method': 'post', 'value': "{'username':'chenyanna','password''123456','repassword':'123456'}", 'except': 0.0, 'real': '', 'status': ''}, 
    {'id': 3.0, 'interfaceUrl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'Method': 'Get', 'value': "{'username':'zhuxiaodong'}", 'except': 0.0, 'real': '', 'status': ''}]
'''
    @data(*case_data)

    def test_case(self,value):

        self.ch = ConfigHttp(**value)
        self.Eresult = self.ch.expect_result
        self.case_num = self.ch.case_num
        real = self.ch.run()
        # 断言
        # print(re.json())
        # real = re.json()['errorCode']

        self.assertEqual(real, int(self.Eresult), msg='预期结果不符合，用例失败')



    # 3.结束工作
    @classmethod
    def tearDownClass(cls):
        pass
    def tearDown(self):
        pass


if __name__ == '__main__':
     unittest.main()
    #TestCaseClass()