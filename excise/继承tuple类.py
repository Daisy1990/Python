#coding:utf-8
'''继承tuple类'''
class Foo(tuple):

    def __new__(cls,a,b):
        return super(Foo,cls).__new__(cls,tuple([a,b]))

    def __init__(self,a,b):
        super(Foo,self).__init__(a,b)
        self.a = a
        self.b = b

if __name__ == "__main__":
    foo = Foo(3,[4,7])
    print foo
    print foo.a
    print foo.b