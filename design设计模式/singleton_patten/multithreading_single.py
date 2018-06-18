import threading


class Singleton(object):
    __instant = None;
    __lock = threading.Lock();

    def __new__(self):
        print("111 new")
        if (Singleton.__instant == None):
            Singleton.__lock.acquire();
            if (Singleton.__instant == None):
                print("001 create")
                Singleton.__instant = object.__new__(self);
            Singleton.__lock.release()
        return Singleton.__instant

    def __init__(self):
        print("0000 init")
        self.name = "111"


if __name__ == '__main__':

    s1 = Singleton()
    s2 = Singleton()

    print(s1.name)
    print(s2.name)
    s1.name = '222'
    print(id(s1), id(s2))
    print(s2.name)