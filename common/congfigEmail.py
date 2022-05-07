'''
功能：发送邮件
编写人：chenyanna
实现步骤：
    1.配置邮箱属性
    2.设置邮箱主题
    3.设置使用的邮箱服务器
    4.准备登录的邮箱用户名和密码
    5.准备附件文件并读取
    6.组装邮件内容
    7.登录并发送
'''
from common.Log import log, logger
import os.path
import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

from common.readConfiginifile import ReadConfigIni


rci = ReadConfigIni()
email_config = rci.readEmail()

class configEmail():
    pass

    def __init__(self):
        # 配置邮箱属性

        self.sender = rci.readEmail('sender')
        self.receiver = rci.readEmail('receiver')
        # 邮件主题
        self.t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.subject = rci.readEmail('subject') + self.t
        # 邮箱服务器
        self.smtpserver = rci.readEmail('smtpserver')
        # 登录邮箱的用户名和密码
        self.username = rci.readEmail('username')
        self.password = rci.readEmail('password')
        #self.content = 'Python测试结果发送邮件......'


    def sendAttachEmail(self,report_file):

        # 读取html内容
        global s
        with open(report_file,'rb') as f:
            mail_body = f.read()

            #组装邮件内容和标题
            msg = MIMEMultipart()
            #附件相关
            att = MIMEText(mail_body, 'plain', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment; filename="report1.html"'
            msg.attach(MIMEText('Hi ALL,\n  附件为自动化测试报告，请查收! \n  自动发送，无需回复。', 'plain', 'utf-8'))
            msg.attach(att)
        msg['Subject'] = Header(self.subject, 'utf-8')
        msg['From'] = self.sender
        msg['To'] = self.receiver

        #登录并发送邮件

        try:
            s = smtplib.SMTP()
            s.connect(self.smtpserver)
            s.login(self.username,self.password)
            s.sendmail(self.sender,self.receiver,msg.as_string())
        except Exception as msg:
            print(u"邮件发送失败！%s"% msg)
        else:
            logger.info("邮件发送成功！")
        finally:
            s.quit()
if __name__ == '__main__':
    report_dir = os.path.dirname(os.path.dirname(__file__)) + '/report/report.html'
    ce = configEmail()
    ce.sendAttachEmail(report_dir)