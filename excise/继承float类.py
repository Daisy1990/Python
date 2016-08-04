#coding:utf-8
'''
round四捨五入 2爲保留兩位小數
繼承float類

'''
class RoundFloat(float):
    def __new__(cls,val):
        return float.__new__(cls,round(val,2))

p1 = RoundFloat(2.89)
print p1
#打印出來是2.89

p2 = RoundFloat(2.847)
print p2
#打印出來是2.85

p3 = RoundFloat(2.897)
print p3
#打印出來是2.9  後面的0不显示