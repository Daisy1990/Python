#coding:utf-8

class Foo(object):
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

list1 = [2,5,8,6,5]
p = Foo(list1)

for item in p:
    print item
