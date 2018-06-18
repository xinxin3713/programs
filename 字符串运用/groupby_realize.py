class groupby(object):
    def __init__(self,iterable,key=None):
        if key is None:
            key = lambda x:x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self

    def __next__(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)
            self.currkey =self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return  (self.currkey,self._grouper(self.tgtkey))
    def _grouper(self,tgtkey):
        while self.currkey == tgtkey:
            yield  self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)


for k, g in groupby('AAAABBBCCD'):
     print(k,g)
     for item in g:
         print(item)
     print("**** END OF GROUP ***\n")

def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

print(list(product('ABCD', 'xy')))