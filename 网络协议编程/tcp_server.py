#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2017/5/13"
import socket
import threading
import time

def tcplink(sock,addr):

    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        # 接收最大1024个字节的数据
        data = sock.recv(1024)
        time.sleep(1)
        # 当接收到 exit 之后，退出获取数据的循环
        if not data or data.decode('utf-8') == 'exit':
            break
        # 发送 一个数据到客服端
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

    # 关闭当前连接
    sock.close()
    print('Connection from %s:%s closed.' % addr)


#1 初始化socket
s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2 绑定IP和端口
s_socket.bind(('127.0.0.1',6789))
#3设置允许连接数量
s_socket.listen(5)
#4 等待连接
while True:
    #获得连接到服务器的socket和ip
    #如果有多个连接请求,用多线程来处理
    fd, addr = s_socket.accept()

    #5 接受消息,发送消息 用函数处理
    t = threading.Thread(target=tcplink ,args=(fd,addr))
    t.start()
