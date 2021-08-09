import sys
sys.path.append("/home/test/zhongKe/")
from commom.api_asser import  *
from commom.send_email import *

Email().sendEmail()

pytest.main(['--html=../report/test_x.html', '../commom//api_asser.py'])
Test_Case().test_home_page()


