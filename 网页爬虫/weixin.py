#!/usr/bin/env python
# _*_coding:utf-8 _*_
import re
import time

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/5/21"
import requests
import urllib3

s = requests.session()
s.trust_env = False
s.verify = False
urllib3.disable_warnings()
s.proxies = {'https': '127.0.0.1:8800'}
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
def get_13_time():
    '''
    获取13个数字的时间措
    :return:
    '''
    return str(int(time.time()*1000))
def get_all_str_by_text_multi(p, text):
    '''
    正则匹配出内容
    :param p: 正则表达式
    :param text:
    :return:
    '''
    l = re.findall(p, text, re.M | re.S)
    return l
def login():
    # request home
    url = 'https://wx.qq.com/'
    requests.get(url)
    #get code,uuid
    url='https://login.wx.qq.com/jslogin'
    params = {
        'appid': 'wx782c26e4c19acffb',
        'redirect_uri': 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage',
        'fun': 'new',
        'lang': 'zh_CN',
        '_': get_13_time(),
    }
    r = s.get(url,params = params)
    uuid = get_all_str_by_text_multi('window.QRLogin.uuid = "(.*?)";', text)
    code = get_all_str_by_text_multi('window.QRLogin.code = (.*?);', text)
    print('获取到uuid：', uuid)
    print('获取到code：', code)
    # get qrcode
    url = 'https://login.weixin.qq.com/qrcode/'+uuid
    r = s.get(url)
    with open('qrcode.jpg','wb')as f:
        f.write(r.content)

    print('get qrcode')

    #判断手机扫描是否成功
    url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login'
    _time = int(get_13_time())
    for _ in range(30):

        params = {
            'loginicon': 'true',
            'uuid': uuid,
            'tip': '1',
            'r': ~int(time.time()),
            '_': str(_time + 1),
        }
        r = s.get(url,params =params)
        code = get_all_str_by_text_multi('window.code = (.*?);',r.text)[0]

    if




if __name__=='__main__':
    login()
    #
    #
    #
    # url = 'https://wx.qq.com/'
    # r = s.get(url)
    # params = {
    #     'appid': 'wx782c26e4c19acffb',
    #     'redirect_uri': 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage',
    #     'fun': 'new',
    #     'lang': 'zh_CN',
    #     '_': get_13_time(),
    # }
    # url = 'https://login.wx.qq.com/jslogin'
    # r = s.get(url, params=params)
    # text = r.text
    # print(text)
    # uuid = get_all_str_by_text_multi('window.QRLogin.uuid = "(.*?)";', text)
    # code = get_all_str_by_text_multi('window.QRLogin.code = (.*?);', text)
    # print('获取到uuid：', uuid)
    # print('获取到code：', code)