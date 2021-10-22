# import sys
# sys.path.append("/home/test/zhongKe/")

from commom.db_handler import *
from commom.handle_request import *
import requests
import json
import pprint
import pytest
import os
class Test_Case:
    def db_data(self):
        db = DBHandler(host='182.92.202.235', port=3306,
                       user='root', password='Root_12root',
                       database='api_data', charset='utf8')
        sql = "SELECT expect,method,url,data FROM test_case "
        data = db.query(sql)
        # print(data)
        # print(url)
        return data

    def api_requests(self):
        #获取数据
        data=self.db_data()
        method=data["method"]
        url = data["url"]
        expect=data["expect"]
        datainfo =data["data"]
        data = json.loads(datainfo)
        #执行requests请求
        run=handle_request()
        res=run.send(url=url,method=method,data=data)
        re=res.json()
        return re


    def test_home_page(self):
        re=self.api_requests()
        data=self.db_data()
        #断言
        expect=data['expect']
        res=re['reason']
        assert res == expect
        print("OK")
        print(re)
        # print(expect)
        return res


        # print(expect)
        # # print(type(re))
    # pytest.main(['--html=report/test_x.html','ceshi2.py'])
if __name__ == '__main__':
    pytest.main(['--html=../report/test_x.html', 'api_asser.py'])
    # Test_Case().test_home_page()
    # pytest.main(['-s', '-q', '--alluredir', '../report/xml', 'api_asser.py'])


# Test_Case().db_data()















