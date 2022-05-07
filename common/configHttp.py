import requests
'''
功能：获取http接口相应的请求方法
编写人：chenyanna
步骤：
1.根据测试数据中的每个接口的请求method决定进行对应的请求
        1-1 get，调用request.get()
            1-1-1 准备接口请求的所有参数
                1-url
                2-params
                3-header（cookie）
                4.timeout
        1-2 post,调用request。post()
            1-2-1 准备接口请求的所有参数
                1-url
                2-data(json)
                3-header（cookie）
                4.timeout
  
    '''

class ConfigHttp():
    def __init__(self, **kwargs):
        self.method = kwargs['Method']
        self.url = kwargs['interfaceUrl']
        self.value = kwargs['value']
        self.expect_result = kwargs['except']
        self.case_name = kwargs['name']
        self.case_num = kwargs['id']
        self.header = {}
        self.timeout = 2

    def run(self):

        if self.method.lower() == 'get':
            return self.__get()
        elif self.method.lower() == 'post':
            return self.__post()
        elif self.method.lower() == 'put':
            return self.__put()
        else:
            print('测试用例编码', self.case_num, '请求的方法不支持')


    def __get(self):
        re = requests.get(url=self.url, params=self.value, headers=self.header, timeout=self.timeout)
        errorCode = re.json()['errorCode']
        return errorCode
    def __post(self):
        re = requests.post(url=self.url, data=eval(self.value), headers=self.header, timeout=self.timeout)
        errorCode = re.json()['errorCode']
        return errorCode

    def __put(self):
        re = requests.post(url=self.url, data=eval(self.value), headers=self.header, timeout=self.timeout)
        errorCode = re.json()['errorCode']
        return errorCode
