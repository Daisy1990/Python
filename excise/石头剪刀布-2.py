#coding:utf-8
import random

guess_list = ['石頭','剪刀','布']
guize_list = [('布','石頭'),('石頭','剪刀'),('剪刀','布')]

def chuquan():
    computer = random.choice(guess_list)
    print computer
    while True:
        try:
            people = raw_input("請輸入石頭 剪刀 布：\n")
            if people not in guess_list:
                print '輸入不匹配，'
                continue
            if computer == people:
                print '平手'
            elif (computer,people) in guize_list:
                print '電腦贏'
            else:
                print '人贏'
                break
        except (KeyboardInterrupt,EOFError):
                print '異常錯誤'
def main():
    while True:
        chuquan()
        try:
            op = raw_input("再來一局?[y]:").lower()
            if (op == 'n'):
                break
        except (KeyboardInterrupt,EOFError):
            print '異常錯誤'
if __name__ == '__main__':
    main()
