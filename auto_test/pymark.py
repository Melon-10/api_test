import sys
sys.path.append("/home/test/auto_1213/")
import pytest
import requests
import json
from auto_test.db_handler import *
from auto_test.handle_request import *

class Test_data:
    def db_data(self):
        db = DBHandler(host='182.92.202.235', port=3306,
                       user='root', password='Root_12root',
                       database='api_data', charset='utf8')
        sql = "SELECT expect,method,url,data FROM test_case "
        test_data = db.query(sql)
        print(test_data)
        return test_data

test_data=Test_data().db_data()
run = handle_request()

class Test_Case:
    @pytest.mark.parametrize('number', test_data)
    def test_equal(self,number):
        method = number["method"]
        url = number["url"]
        expect = number["expect"]
        datainfo = number["data"]
        data = json.loads(datainfo)
        # data = json.loads(datainfo)
        # print(method,url,expect)
        # run = handle_request()
        res = run.send(url=url, method=method, data=data)
        re = res.json()
        print(re)
        res = re['reason']
        assert res == expect
        print("ok")
    # print(expect)

if __name__ == '__main__':
    pytest.main(['--html=../report/test_x.html', 'pymark.py'])