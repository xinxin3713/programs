#!/usr/bin/env python
# _*_coding:utf-8 _*_
import random
import re
import urllib3
import datetime

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/6/8"
import base64
import requests
import time

urllib3.disable_warnings()
def get_all_str_by_text_multi(p, text):
    '''
    正则匹配出内容
    :param p: 正则表达式
    :param text:
    :return:
    '''
    l = re.findall(p, text, re.M | re.S)
    return l

def to_encode_gbk(text):
    t =str(text.encode('gbk'))[1:]
    return t.upper().replace('\X','%')

def get_hotel(city,city_no,hotel_name):



    headers ={
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://hotel.fliggy.com/hotel_list3.htm?_input_charset=&_output_charset=&searchBy=&market=0&previousChannel=&cityName=%B1%B1%BE%A9&city=110100&_fmd.h._0.r=&checkIn=2018-06-11&checkOut=2018-06-12&keywords=%CB%D98',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    s = requests.session()
    s.verify = False
    s.trust_env =False
    s.headers = headers

    city_name = to_encode_gbk(city)
    city_no =city_no
    hotel_name = to_encode_gbk(hotel_name)
    start = datetime.date.today() + datetime.timedelta(random.choice([0, 1, 2]))
    end = datetime.date.today() + datetime.timedelta(random.choice([0, 1, 2]))

    url = f'https://hotel.fliggy.com/hotel_list3.htm?_input_charset=&_output_charset=&searchBy=&market=0&previousChannel=&cityName={city_name}&city={city_no}&_fmd.h._0.r=&checkIn={start}&checkOut={end}&keywords={hotel_name}'
    r = s.get(url)
    text = r.text
    print(text)


    '''
    <div class="list-row J_ListRow J_LazyZoom" data-righttitle="速8" data-idx="1" data-shid="53271010" data-lng="116.388738" data-lat="39.888216" data-name="速8酒店北京前门虎坊桥地铁站店">
                        <div class="row-box clearfix">
                            <div class="row-left fleft">
                                                                <a href="//hotel.fliggy.com/hotel_detail2.htm?spm=181.7087309.0.0.1244ec74K3zqbK&amp;searchBy=&amp;shid=53271010&amp;city=110100&amp;checkIn=2018-06-11&amp;checkOut=2018-06-12&amp;market=0&amp;previousChannel=&amp;searchId=e0b76a396b28433ea612f28117685a8b&amp;filterByRoomTickets=false&amp;activityCode=&amp;roomNum=1&amp;aNum_1=2&amp;cNum_1=0" target="_blank" data-spm-anchor-id="181.7087309.0.0">
                                        <img src="//img.alicdn.com/bao/uploaded/i3/TB1Ls0USXXXXXXDXpXX9t_z8XXX_020854.jpg_210x1000.jpg" alt="速8酒店北京前门虎坊桥地铁站店" data-spm-anchor-id="181.7087309.0.i2.1244ec74K3zqbK"></a>
                                                            <i class="credit-icon">信用住</i>        
    '''


    p='<div class="list-row J_ListRow J_LazyZoom'+ '.*?data-shid="(.*?)"'+'.*?  <i class="credit-icon">(.*?)</i> '
    r = get_all_str_by_text_multi(p,text)
    print(r)

if __name__ == '__main__':
    #get_hotel('北京',110100, '如家')
    time.sleep(random.random() * 3)
    get_hotel('兰州', 620100, '速8')