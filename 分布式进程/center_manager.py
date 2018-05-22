#!/usr/bin/env python
# _*_coding:utf-8 _*_
import queue
import time

from multiprocessing import Process

from import_code.分布式进程.URLManager import UrlManager
from import_code.分布式进程.data_save import DataOutput

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/4/4"
from multiprocessing.managers import BaseManager


class NodeManager(object):

    def start_manager(self, url_q, result_q):
        '''
        创建一个分布式管理器
        :param url_q: url队列
        :param result_q: 结果队列
        :return: manager
        '''
        #利用register把创建的两个队列注册在网络上,
        #将Queue对象在网络中暴露
        BaseManager.register('get_task_queue', callable=lambda: url_q)
        BaseManager.register('get_result_queue', callable=lambda: result_q)
        #BaseManager对象的初始化,地址和口令
        manager = BaseManager(address=('', 8002), authkey='baike'.encode('utf-8'))
        return manager

    def url_manager_proc(self, url_q, conn_q, root_url):
        '''
        url管理进程:把从conn_q 队列获取到新的url 提交给管理器,
        去重以后放入url_q队列,传递给爬虫节点
        :param url_q:
        :param conn_q:
        :param root_url:主网站url
        :return:
        '''

        url_manager = UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            #获取新的url
            while (url_manager.has_new_url()):
                new_url = url_manager.get_new_url()
                url_q.put(new_url)
                print('old_url = ', url_manager.old_url_size())
                #当爬取2000个链接后就关闭,并保存进度
                if (url_manager.old_url_size() > 2000):
                    #通知爬行节点结束
                    url_q.put('end')
                    print('控制节点发起结束通知!')
                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                    return
            #将从result_solve_proc获取到的url添加到url管理器
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    url_manager.add_new_urls(urls)

            except BaseException:

                time.sleep(.1)

    def result_solve_proc(self,result_q,conn_q,store_q):
        '''
        #数据提取进程从result_q队列读取返回的数据,并将数据中的url添加到conn_q队列
        #交给url管理进程,将文章标题和摘要添加到store_q队列交给数据存储进程
        :param result_q:
        :param conn_q:
        :param store_q:
        :return:
        '''
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls']=='end':
                        #结果分析进程接收end通知返回
                        store_q.put('end')
                        return
                    #url为set类型,能自动去重
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])

                else:
                    time.sleep(.1)
            except BaseException:
                time.sleep(.1)

    def store_proc(self,store_q):
        '''
        数据存储进程从store_q队列中读取数据,并调用存储器进行数据存储
        :param store_q:
        :return:
        '''
        output = DataOutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print('存储进程接受通知然后结束')
                    output.output_end(output.filepath)
                    return
                output.store_data(data)
            else:
                time.sleep(.1)



if __name__== "__main__":
    #启动分布式管理器,url管理进程,数据提取进程,数据存储进程
    # 并初始化队列
    url_q =queue.Queue()
    result_q = queue.Queue()
    store_q =queue.Queue()
    conn_q = queue.Queue()

    node = NodeManager()
    manager = node.start_manager(url_q,result_q)
    url = 'http://baike.baidu.com/view'
    url_manager_proc = Process(target=node.url_manager_proc,args=(url_q,conn_q,url,))

    result_solve_proc =Process(target=node.result_solve_proc,args=(result_q,conn_q,store_q,))
    store_proc = Process(target=node.store_proc,args=(store_q,))
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.get_server().server_forever()

