from api_asser import *

if __name__ == '__main__':
    pytest.main(['--html=report/test_x.html', 'api_asser.py'])
    Test_Case().test_home_page()