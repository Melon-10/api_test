import sys
sys.path.append("/home/test/api_test/")
import smtplib
from email.mime.text import MIMEText
from email.header import Header
class Email:

    def sendEmail(self):
        mail_host = "smtp.163.com"  # 设置服务器
        mail_user = "17753679317@163.com"  # 用户名
        mail_pass = "RLEVOMWSWAEKCGIM"  # 授权码，注意不是邮箱登录密码，是上述设置的授权密码！！！
        sender = '17753679317@163.com'
        receivers = ['17753679317@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        message = MIMEText('详细测试结果，请查看http://182.92.202.235/test_x.html', 'plain', 'utf-8')
        message['From'] = "17753679317@163.com"
        message['To'] = "17753679317@163.com"
        subject = '自动化测试执行结果通知'
        message['Subject'] = Header(subject, 'utf-8')

        smtpObj=smtplib.SMTP_SSL()
        smtpObj.connect(mail_host,465)
        smtpObj.set_debuglevel(1)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())

if __name__ == '__main__':
    Email().sendEmail()
    print("邮件发送成功")
