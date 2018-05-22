#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2017/5/11"

import http.client
url = 'music.baidu.com'
conn = http.client.HTTPConnection(url)
conn.request('GET','/')
result = conn.getresponse()
print(result.status,result.reason)
# data = result.read()
while not result.isclosed():
    print(result.read(200))
conn.request("GET", "/artist")
result2 = conn.getresponse()
print(result2.status,result2.reason)
print(result2.read())
conn.close()

import http.client,urllib.parse
params = urllib.parse.urlencode({'@number':12524,'@type':'issue','@action':'show'})
headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
conn = http.client.HTTPConnection("bugs.python.org")
conn.request("POST",'',params,headers)
respone = conn.getresponse()
print(respone.status,respone.reason)
data = result2.read()
print(data)
conn.close()

