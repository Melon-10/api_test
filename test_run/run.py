import sys
sys.path.append("/home/test/api_test/")
from auto_test.pymark import *
pytest.main(['--html=../report/test_x.html', '../auto_test//pymark.py'])