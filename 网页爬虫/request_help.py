#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from urllib.parse import parse_qsl
from datetime import date,timedelta
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
    # if headers_raw_l[-1].startswith('Cookie'):
    #     headers_raw_l.pop(-1)

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
Upgrade-Insecure-Requests	1
User-Agent	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Accept	text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer	https://hotel.fliggy.com/hotel_list3.htm?_input_charset=&_output_charset=&searchBy=&market=0&previousChannel=&cityName=%B1%B1%BE%A9&city=110100&_fmd.h._0.r=&checkIn=2018-06-11&checkOut=2018-06-12&keywords=%CB%D98
Accept-Encoding	gzip, deflate, br
Accept-Language	zh-CN,zh;q=0.9
Cookie	cna=BMc4E0D1sksCAXlFXoYnGfv2; hng=CN%7Czh-CN%7CCNY%7C156; t=41eb842f8063a83a1ab8bce296752dac; _tb_token_=73b57b7ee9be6; cookie2=33484079c1fd74ed0f6e8d9ce532c580; UM_distinctid=163dfd07d1c149-0ac3f1b70dad5f-3a614f0b-144000-163dfd07d1d7ae; CNZZDATA1253581663=1556969732-1528467023-https%253A%252F%252Fwww.fliggy.com%252F%7C1528467023; JSESSIONID=E4B604952989616A5FB9E9564A72A022; isg=BOjoToynJ5FLjQsVwMzze_OtudY6uUagkwpiZKIZDWNW_YlnSiISq9z_8JUNdATz
 '''
    print_dict_from_copy_headers(text_fiddler)


    # url_params = 'token=5a1fe73ef0892cff6e0f920ea18077f5&tpl=mn&apiver=v3&tt=1521463458242&fr=login&loginversion=v4&vcodetype=f015b0hy0qvcbwWlmY1AjwsYOr7B%2B%2Fy8oI5WUh9RUFKopq83%2BU%2BZ%2FZpAbumIALvlxxPf9fFWu3JCDqJCwcjeElWMI7n%2B0Ow4kYiB&traceid=DCDEE301&callback=bd__cbs__hsvzb2'
    # print_url_params_new(url_params) %CB%D98'

    t =str('速8'.encode('gbk'))[1:]
    city = t.upper().replace('\X','%')
    print(city)






