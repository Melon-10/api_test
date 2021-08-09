import sys
sys.path.append("/home/test/zhongKe/")
from commom.tiaoshi import  *
from commom.send_email import *

Email().sendEmail()

pytest.main(['--html=../report/test_x.html', '../commom//tiaoshi.py'])
Test_Case().api_requests()


