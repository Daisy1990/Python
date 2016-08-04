#coding:utf-8
import random
'''
craps掷骰子游戏
掷两个骰子(每个骰子有六面，1～6个点)
计算两个骰子之和
1、如果和为7或者11，玩家赢，庄家输；
2、如果和为2、3或12，玩家输，庄家赢；
3、如果和为4、5、6、8、9或10，则这个值称为“点数” t，重新掷骰子
    a.如果和为“点数” t，则玩家赢，庄家输；
    b.如果和为7，则玩家输，庄家赢；
    c.否则，重新掷骰子 
write by Daisy1990
'''
t_list =[4,5,6,8,9,10]
def f_sum():
    player = random.randint(1,6)
    banker = random.randint(1,6)
    return (player + banker)
def youxi():
    sum =f_sum()
    print sum
    if sum == 7 or sum == 10:
        print "player win"
    if sum == 2 or sum == 12 or sum == 13:
        print 'banker win'
    if sum in t_list:
        while True:
            print "需要重新投擲骰子"
            sum2 = f_sum()#重新投擲骰子
            print '新骰子點數和=',sum2
            if sum2 in t_list:
                print 'player win'
                break
            elif sum2 == 7:
                print 'banker win'
                break
            continue
youxi()
