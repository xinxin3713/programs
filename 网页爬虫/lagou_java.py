#!/usr/bin/env python
# _*_coding:utf-8 _*_
import time

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/5/25"
import requests
from lxml import etree




headers = {

        'Connection': 'keep-alive',
        'Content-Length': '65',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Anit-Forge-Token': 'None',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'

        }

data = {
    'first': False,
    'pn':1,
    'kd': 'java',
}

def get_job(data):
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    page = requests.post(url=url, headers=headers, data=data)
    page.encoding = 'utf-8'
    result = page.json()
    jobs = result['content']['positionResult']['result']
    for job in jobs:
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

        detail_url = 'https://www.lagou.com/jobs/{}.html'.format(positionId)
        response = requests.get(url=detail_url, headers=headers, cookies=cookies)
        response.encoding = 'utf-8'
        tree = etree.HTML(response.text)
        desc = tree.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')

        print(companyFullName)
        print('%s 拉勾网链接:-> %s' % (companyShortName, detail_url))

        print('职位：%s' % positionName)
        print('职位类型：%s' % firstType)
        print('薪资待遇：%s' % salary)
        print('职位诱惑：%s' % positionAdvantage)
        print('地区：%s' % district)
        print('类型：%s' % jobNature)
        print('工作经验：%s' % workYear)
        print('学历要求：%s' % education)
        print('发布时间：%s' % createTime)
        x = ''
        for label in positionLables:
            x += label + ','
        print('技能标签：%s' % x)
        print('公司类型：%s' % industryField)
        for des in desc:
            print(des)


def url(data):
    for x in range(1,3):
        data['pn'] = x
        time.sleep(1)
        get_job(data)

if __name__ == '__main__':
    url(data)

