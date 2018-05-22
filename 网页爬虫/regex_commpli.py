import base64
import random
import re
#爬虫工具包
import time
from urllib.parse import quote

def get_all_str_by_text_multi(p, text):
    '''
    正则匹配出内容
    :param p: 正则表达式
    :param text:
    :return:
    '''
    l = re.findall(p, text, re.M | re.S)[0]
    return l

text = '''<html><head><title>302 Moved Temporarily</title></head>
<body bgcolor="#FFFFFF">
<p>This document you requested has moved temporarily.</p>
<p>It's now at <a href="http://www.pss-system.gov.cn/sipopublicsearch/portal/uilogin-loginSuccess.shtml?params=991CFE73D4DF553253D44E119219BF31366856FF4B15222669397E093A956A2C&amp;j_loginsuccess_url=">http://www.pss-system.gov.cn/sipopublicsearch/portal/uilogin-loginSuccess.shtml?params=991CFE73D4DF553253D44E119219BF31366856FF4B15222669397E093A956A2C&amp;j_loginsuccess_url=</a>.</p>
</body></html>'''

p = '<a href="(.*?)"'
print(get_all_str_by_text_multi(p, text)[0])


def get_13_time():
    '''
    获取13个数字的时间措
    :return:
    '''
    return str(int(time.time()*1000))

def encrpty_user(user):
    '''
    user加密
    :param user:
    :return:
    '''
    return base64.b64encode(quote(user).encode()).decode()

def gen_random_hex_str(num, uppered = False):
    '''

    :param num:
    :param uppered:
    :return:
    '''
    s = ''
    for _ in range(num):
        s += random.choice('0123456789abcdef')

    if uppered:
        s = s.upper()

    return s


