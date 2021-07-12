from commom.db_handler import *
from commom.handle_request import *
import requests
import json
import pprint
import pytest
import allure
import os
@allure.feature("接口测试")
class Test_Case:
    def db_data(self):
        db = DBHandler(host='127.0.0.1', port=3306,
                       user='root', password='admin',
                       database='api_data', charset='utf8')
        sql = "SELECT expect,method,url,data FROM test_case where case_id=2"
        data = db.query(sql)
        # print(data)
        # print(url)
        return data

    # @allure.story('执行requests')
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
        return res
        # print(expect)
        # # print(type(re))
    # pytest.main(['--html=report/test_x.html','ceshi2.py'])
if __name__ == '__main__':
    # pytest.main(['--html=../report/test_x.html', 'api_asser.py'])
    pytest.main(['-s', '-q', '--alluredir', '../report/xml', 'api_asser.py'])

    # Test_Case().test_home_page()















