import threading
import time

# def print_time(threadName,delay):
#     '''
#     threadName 线程 ,delay 延迟时间
#     :param threadName:
#     :param delay:
#     :return:
#     '''
#     count = 0
#     for i in range(4):
#         time.sleep(delay)
#         print('%s:%s' %(threadName,time.ctime(time.time())))
#
# try:
#     t1 = threading.Thread(target=print_time,args = ('线程-1',2,))
#     t2 = threading.Thread(target=print_time,args = ('线程-2',4,))
#     t1.start()
#     t2.start()
# except:
#     print('Error:')


def action(arg):
    '''
    setDaemon(True)设置线程为后台线程,主程序结束后台程序不管什么情况都结束
    :param arg:
    :return:
    '''
    time.sleep(1)
    print('sub thread start the thread name is %s' %threading.currentThread().getName())
    print('the arg is %s' %arg)
    time.sleep(1)

for i in range(4):
    t = threading.Thread(target=action,args=(i,))
    # t.setDaemon(True) #设置线程为后台线程
    t.start()
print('main thread end!')