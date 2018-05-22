#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/4/3"

import time
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
server_addr = '127.0.0.1'
print('connect to server %s' %server_addr)
m = QueueManager(address=(server_addr,8001),authkey='qiye'.encode('utf-8'))
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()

while(not task.empty()):
    image_url = task.get(True,timeout=5)
    print('run task dowmload %s' %image_url)
    time.sleep(1)
    result.put(image_url)
print('worker exit')