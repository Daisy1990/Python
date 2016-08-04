#coding:utf-8
"""
此類是用來抽取日誌文件中的ip地址
"""

class findIp(object):

    def __init__(self,path):
        self.textfile = path

    def getIp(self,kwstr):
        file1 = open(self.textfile,'r')
        iplist = []
        for line in file1:
            findIndex = line.find(kwstr)
            if findIndex>0:
                iplist.append(line[:findIndex].strip())
        return iplist

sougou = findIp('/home/shixx/mypython/9/ip.txt')
sougouip = sougou.getIp("\"Sogou web spider")
print list(set(sougouip))
