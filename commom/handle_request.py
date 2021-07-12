# -*- coding: utf-8 -*-

import requests

class handle_request:
    def send(self,url,method,data=None,header=None):
        method=method.lower()
        if method =="post":
            return requests.post(url=url,data=data,headers=header)
        elif method =="get":
            return requests.get(url=url, params=data,headers=header)



