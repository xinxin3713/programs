#!/usr/bin/env python
# _*_coding:utf-8 _*_
import csv
import time
from lxml import etree

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/5/25"


import requests
import urllib3
import random
urllib3.disable_warnings()

session =requests.session()
session.verify = False
session.trust_env = False

session.proxies = {'https':'127.0.0.1:8800'}

headers ={
    'Connection': 'keep-alive',
    # 'Content-Length': '82',
    'Origin': 'https://www.lagou.com',
    # 'X-Anit-Forge-Code': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Anit-Forge-Token': 'None',
    'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'user_trace_token=20180420181028-17385fc8-8832-4449-b979-da988797a1a9; _ga=GA1.2.898594576.1524219030; LGUID=20180420181029-0db5d65b-4483-11e8-8eec-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAAAIAACBI92D22284F04F98AF8D9DB5ACFE6B9165; LGSID=20180525093710-244fdd53-5fbc-11e8-98ec-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1PnCV68FLOCoNvZ9ln_pa7cdZNRLyvhWPCZDeG0KtaC%26wd%3D%26eqid%3Dc33847590004b1bc000000035b0768b3; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1526007897,1526007914,1526722366,1527212233; _gid=GA1.2.1186305427.1527212233; TG-TRACK-CODE=search_code; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1527213045; LGRID=20180525095042-0869f796-5fbe-11e8-8aec-5254005c3644; SEARCH_ID=f2756a6c35744468882e32bfede5106b'
}



def request_load():
    url = 'https://www.lagou.com/'
    r = session.get(url)
    print('sucess')



def get_job(job,num=1):

    first = 'true' if num==1 else 'false'
    json = {
        'first': first,
        'pn': str(num),
        'kd':job #'数据分析工程师'
    }

    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    r = session.post(url,data=json)
    r.encoding ='utf-8'
    page = r.json()
    try:
       result =page['content']['positionResult']['result']
    except:
        pass
    for job in result:
        companyShortName = job['companyShortName']
        positionId = job['positionId']  # 主页ID
        companyFullName = job['companyFullName']  # 公司全名
        companyLabelList = job['companyLabelList']  # 福利待遇
        companySize = job['companySize']  # 公司规模
        industryField = job['industryField']
        createTime = job['createTime']  # 发布时间
        district = job['district']  # 地区
        education = job['education']  # 学历要求
        financeStage = job['financeStage']  # 上市否
        firstType = job['firstType']  # 类型
        secondType = job['secondType']  # 类型
        formatCreateTime = job['formatCreateTime']  # 发布时间
        publisherId = job['publisherId']  # 发布人ID
        salary = job['salary']  # 薪资
        workYear = job['workYear']  # 工作年限
        positionName = job['positionName']  #
        jobNature = job['jobNature']  # 全职
        positionAdvantage = job['positionAdvantage']  # 工作福利
        positionLables = job['positionLables']  # 工种

        detail_url = f'https://www.lagou.com/jobs/{positionId}.html'
        # session.headers=headers
        # response = session.get(url)
        # response.encoding='utf-8'
        # print(response.text)
        # tree = etree.HTML(response.text)
        # desc = tree.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')
        #
        # print(desc)
        #
        # print(companyFullName)
        # print('%s 拉勾网链接:-> %s' % (companyShortName, detail_url))
        #
        # print('职位：%s' % positionName)
        # print('职位类型：%s' % firstType)
        # print('薪资待遇：%s' % salary)
        # print('职位诱惑：%s' % positionAdvantage)
        # print('地区：%s' % district)
        # print('类型：%s' % jobNature)
        # print('工作经验：%s' % workYear)
        # print('学历要求：%s' % education)
        # print('发布时间：%s' % createTime)
        # x = ''
        # for label in positionLables:
        #     x += label + ','
        # print('技能标签：%s' % x)
        # print('公司类型：%s' % industryField)
        # for des in desc:
        #     print(des)
        with open('数据分析.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow((companyFullName, positionName, firstType, salary, positionAdvantage, district, jobNature, workYear, education, industryField))






if __name__=='__main__':
    request_load()
    time.sleep(2*random.random())
    # with open('数据分析.csv', 'w', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(('公司名称', '职位', '职位类型','薪资待遇','职位诱惑','地区','类型','工作经验','学历','公司类型'))
    session.headers = headers

    for i in range(25,40):
        time.sleep(i * random.random())
        get_job('数据分析工程师',i)