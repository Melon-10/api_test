import sys
sys.path.append("/home/test/api_test/")
from auto_test.pymark import *
from auto_test.send_email import *
pytest.main(['--html=../report/test_x.html', '../auto_test//pymark.py'])
Email().sendEmail()
print("邮件发送成功了")
