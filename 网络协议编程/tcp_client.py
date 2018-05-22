#!/usr/bin/env python
# _*_coding:utf-8 _*_
import time

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2017/5/13"

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',6789))
print(client.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    client.send(data)
    time.sleep(10)
    print(client.recv(1024).decode('utf-8'))
client.send(b'exit')
client.close()