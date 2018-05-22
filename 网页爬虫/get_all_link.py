#!/usr/bin/env python
# _*_coding:utf-8 _*_
import re
from urllib.parse import urlparse
from urllib.request import urlopen

from bs4 import BeautifulSoup

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/3/30"

all_ext_links = set()
all_int_links = set()

def get_internal_links(bs_obj, includer_url):
    includer_url = urlparse(includer_url).scheme + '://' + urlparse(includer_url).netloc
    internal_links = []
    links = bs_obj.find_all('a', href=re.compile("^(/|.*" + includer_url + ")"))
    for link in links:
        href = link.attrs['href']
        if href is not None:
            if href not in internal_links:
                if (href.startswith('/')):
                    internal_links.append(includer_url + href)
                else:
                    internal_links.append(href)

    return internal_links

def get_external_links(bs_obj,excude_url):
    external_links = []
    links = bs_obj.find_all('a',href=re.compile('^(http|www)((?!'+excude_url+').)*$'))
    for link in links:
        href = link.attrs['href']
        if href is not None:
            if  href not in  external_links:
                external_links.append(href)
    return external_links

def get_iners_extern_links(url):
    html = urlopen(url)
    bs_obj = BeautifulSoup(html,'lxml')

def get_all_external_links(url):
    html = urlopen(url)
    bs_obj = BeautifulSoup(html)
    internal_links = get_internal_links(bs_obj,url)
    external_links = get_all_external_links(bs_obj,url)


if __name__=='__main__':
    url = 'http://music.baidu.com/'
    html = urlopen(url)
    bs_obj = BeautifulSoup(html,'lxml')
    links =get_external_links(bs_obj,'http://music.baidu.com')
    for link in links:

        print(link)
