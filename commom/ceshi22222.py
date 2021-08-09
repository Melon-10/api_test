import sys
sys.path.append("/home/test/zhongKe/")

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
        datalist = db.query(sql)
        return datalist

    def test_requests(self):
        #获取数据
        datalist=self.db_data()
        for data in datalist:
            method=data["method"]
            url = data["url"]
            expect=data["expect"]
            datainfo =data["data"]
            data = json.loads(datainfo)
            #执行requests请求
            run=handle_request()
            res=run.send(url=url,method=method,data=data)
            re=res.json()
            #从请求中提取断言字段
            res = re['reason']
            #断言
            assert res == expect
            print("OK"),print(re)

if __name__ == '__main__':
    pytest.main(['--html=../report/test_x.html', 'tiaoshi.py'])
    # Test_Case().api_requests()
# Test_Case().api_requests()