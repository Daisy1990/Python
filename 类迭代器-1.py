#coding:utf-8
'''
迭代器是一个实现迭代协议到容器
'''

class MyIterator(object):
    """docstring for className"""
    def __init__(self,step):
        self.step = step

    def next(self):
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self

print list(MyIterator(9))
# p = MyIterator(3)
# print p.next()
# print p.next()
# print p.next()
# # print p.next()
#
# for item in MyIterator(13):
#     print item
