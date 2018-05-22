#!/usr/bin/env python
# _*_coding:utf-8 _*_

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/5/21"


from time import sleep
import requests
# s = input("请主人输入话题")
# while True:
#     resp = requests.post("http://www.tuling123.com/openapi/api", data={"key": "4fede3c4384846b9a7d0456a5e1e2943", "info" : s,})
#     resp = resp.json()
#     sleep(1)
#     print("小鱼:", resp["text"])
#     s = resp["text"]
#     resp = requests.get("http://api.qingyunke.com/api.php", {"key": "free", "appid": 0, "msg": s})
#     resp.encoding = "utf-8"
#     resp = resp.json()
#     sleep(1)
#     print("菲菲:", resp["content"])

headers = {
    'Connection': 'keep-alive',
    # 'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Referer': 'https://www.baidu.com/link?url=25kO5hdcS-zDzN46oI9muhBCPidZ_6-o6wUZPpq24ni&wd=&eqid=a72c7cfe0004b093000000035ab84f57',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

data={
    'r': '1526863292790',
    'skey': '@crypt_ebbbee3a_63b0affde352f79739734f7dde6aa468',
    'sid': 'y4sUlwe4tq+sHMcb',
    'uin': '2752599605',
    'deviceid': 'e739082018716263',
    'synckey': '1_684093519|2_684093605|3_684093582|11_684093123|201_1526863164|1000_1526858402|1001_1526858474|2001_1526471889',
    '_': '1526862958358'
}
url ='https://webpush.wx2.qq.com/cgi-bin/mmwebwx-bin'
session=requests.session()
session.headers = headers
session.verify = False
r = session.get(url,data=data)