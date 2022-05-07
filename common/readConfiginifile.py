'''
描述：读取configini文件内容，获取指定配置项
编写人：chenyanna
实现步骤：
    1.导包
    2.实例化configparse
    3.读取目标文件
    4.提供对外读取某个section的方法
'''

import configparser,os

class ReadConfigIni():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.filepath = os.path.dirname(os.path.dirname(__file__)) + '\\config.ini'
        self.conf.read(self.filepath,encoding='utf-8-sig')

    def readEmail(self,option='Email'):
        # 读取所有section
        # sects = self.conf.sections()
        # 读取options
        # opts = self.conf.options('Email')
        # 读取某个sections下的所有键值对
        # kvs = self.conf.items('Email')
        # 读取某个sections下的某个options
        # sov = self.conf.get('Email','smtpserver')
        if option == 'Email':
            email_data = self.conf.items('Email')
        else:
            email_data = self.conf.get('Email', option)
        #print(email_data)
        return email_data

    def readDatabase(self,option='Database'):

        if option == 'Database':
            email_data = self.conf.items('Database')
        else:
            email_data = self.conf.get('Database', option)
        #print(email_data)
        return email_data

if __name__ == '__main__':
    rci = ReadConfigIni()
    rci.readEmail()
#    rci.readDatabase()