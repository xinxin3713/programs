#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import parse_qsl

__author__ = 'Terry'


def print_headers_raw_to_dict(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" +
        "': '".join(s.strip().split(': ')) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_headers_raw_to_dict_space(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" + "': '".join(s.strip().split('\t') if len(s.strip().split('\t'))>1 else [s.strip(), '']) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_dict_from_copy_headers(headers_raw):
    headers_raw = headers_raw.strip()
    headers_raw_l = headers_raw.splitlines()

    if 'HTTP/1.1' in headers_raw_l[0]:
        headers_raw_l.pop(0)
    if headers_raw_l[0].startswith('Host'):
        headers_raw_l.pop(0)
    if headers_raw_l[-1].startswith('Cookie'):
        headers_raw_l.pop(-1)

    if ':' in headers_raw_l[-1]:
        print_headers_raw_to_dict(headers_raw_l)
    else:
        print_headers_raw_to_dict_space(headers_raw_l)

def print_url_params(url_params):
    s = str(parse_qsl(url_params.strip(), 1))
    print("OrderedDict(\n    " + "),\n    ".join(map(lambda s: s.strip(), s.split("),")))[1:-1] + ",\n)")

def print_url_params_new(url_params):
    l = parse_qsl(url_params.strip(), 1)
    print("{\n    " + "',\n    ".join(map(lambda s: "'"+s[0]+"': '"+s[1], l)) + "',\n}")

if __name__ == '__main__':
    text = '''
	GET /otn/leftTicket/log?leftTicketDTO.train_date=2018-02-13&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CSQ&purpose_codes=ADULT HTTP/1.1
Host: kyfw.12306.cn
Connection	keep-alive
Cache-Control	no-cache
Accept	application/json, text/javascript, */*; q=0.01
If-Modified-Since	0
User-Agent	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
Referer	https://kyfw.12306.cn/otn/leftTicket/init
Accept-Encoding	gzip, deflate, sdch
Accept-Language	zh-CN,zh;q=0.8
Cookie	JSESSIONID=14E3D608CF07BA70F289D01E393C7E50; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=200278538.64545.0000; RAIL_EXPIRATION=1516530260973; RAIL_DEVICEID=f2T-YHHOVgWxXsYXPoB8g7UjWxVhf9LzmzfowiB7x2P-GkCEJhf2RN_7kuULxRf6hyPXYkYac7gFyDGX6MCKruYPxYJFqphkWSqYvcj7YCCkVoj8p0lih_m_7NjXlQK2MzWaUD9aFIFe64cyWO2KLmwSt-2IsihU; current_captcha_type=Z; acw_tc=AQAAAAdFGgkAfQIAwLz+Z7kcj9pHaWAk; _jc_save_fromDate=2018-02-13; _jc_save_toDate=2018-02-13; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u957F%u6C99%2CCSQ; _jc_save_wfdc_flag=dc
    '''

    text_fiddler = '''
Connection	keep-alive
User-Agent	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept	*/*
Referer	https://wx2.qq.com/
Accept-Encoding	gzip, deflate, br
Accept-Language	zh-CN,zh;q=0.9
Cookie	RK=KThVT1zFWn; ptcz=2659cbd5deb8c4545d2e806726bfe70417b8188125aeab02993676e894ffcaf6; pgv_pvid=8678266280; o_cookie=371300491; pac_uid=1_371300491; pgv_pvi=3109582848; webwxuvid=659da594fce3c377087f7fd5bf743d74723d92251293001ea296aeb58d3cc3dca901e35a75c840c313d33a4adf2362fc; LW_uid=U1W572E2P9l809Y9z5q2i5R207; eas_sid=i1s542D2o9W8n9i9H5f321Q9a5; tvfe_boss_uuid=4e0ced2e6a955360; pt2gguin=o0371300491; LW_sid=P1S562A6U8o1032276v685R5P6; wxuin=2752599605; wxsid=y4sUlwe4tq+sHMcb; mm_lang=zh_CN; webwx_data_ticket=gSeSPI6jpG8hMV9y1pxco/MX; webwx_auth_ticket=CIsBENe1npsFGoABQOf9kDYgRrqnejrWOfulvsaVHj0rK99FnYT0MmQo5hfD0SVboCsCpbH1PIAGbeeNOOb7sYjmbHvgEwwfGEHQnSb7xAWu7vBScKmxTwK6g/tXjXkOp8N3vFPpWa/n0Smqx+ZABNb9G/qDgNlTTJ4zBcr49Tn8Tlx5+s3kY9yzdsA=; wxloadtime=1526862955_expired; wxpluginkey=1526858402
  '''

    print_dict_from_copy_headers(text_fiddler)


    # url_params = 'token=5a1fe73ef0892cff6e0f920ea18077f5&tpl=mn&apiver=v3&tt=1521463458242&fr=login&loginversion=v4&vcodetype=f015b0hy0qvcbwWlmY1AjwsYOr7B%2B%2Fy8oI5WUh9RUFKopq83%2BU%2BZ%2FZpAbumIALvlxxPf9fFWu3JCDqJCwcjeElWMI7n%2B0Ow4kYiB&traceid=DCDEE301&callback=bd__cbs__hsvzb2'
    # print_url_params_new(url_params)