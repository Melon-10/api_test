# from ddt import *
import ddt
import sys
sys.path.append("/home/test/zhongKe/")
from commom.db_handler import *
from commom.handle_request import *
import requests
import json
import pprint
import pytest
import os
@ddt.ddt() # 声明此方法使用ddt提供的数据驱动方法
class Test_Case:
    # def db_data(self):
    #     db = DBHandler(host='182.92.202.235', port=3306,
    #                    user='root', password='Root_12root',
    #                    database='api_data', charset='utf8')
    #     sql = "SELECT expect,method,url,data FROM test_case "
    #     datalist = db.query(sql)
    #     # return datalist
    #     print(datalist)
    data=[{'expect': '查询成功!', 'method': 'post', 'url': 'http://apis.juhe.cn/simpleWeather/query', 'data': '{"city":"北京","key":"6aa4bfa8e3f0acdf03cd3dc258538fbc"}'}, {'expect': 'success', 'method': 'get', 'url': 'http://apis.juhe.cn/xzpd/query', 'data': '{"men":"白羊","women":"狮子","key":"491365e396574ead63ad0b074d5f97b1"}'}, {'expect': 'success!', 'method': 'get', 'url': 'http://apis.juhe.cn/gnyj/query', 'data': '{"key":"4429a996355bc8ca3c2296f9d4e98350"}'}]

    @ddt.data(*data)
    def test_requests(self, data):
        print(data)
        method = data["method"]
        url = data["url"]
        expect = data["expect"]
        datainfo = data["data"]
        data = json.loads(datainfo)
        # 执行requests请求
        run = handle_request()
        res = run.send(url=url, method=method, data=data)
        re = res.json()
        # 从请求中提取断言字段
        res = re['reason']
        # 断言
        assert res == expect
        print("OK"), print(re)
pytest.main(['--html=../report/test_x.html', 'tiaoshi.py'])
# if __name__ == '__main__':

