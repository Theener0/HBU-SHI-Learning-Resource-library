"""
题目内容：
猜数游戏。预设一个0~9之间的整数（例如：7），让用户猜一猜并输入所猜的数，
如果大于预设的数，显示“太大”；小于预设的数，显示“太小”，如此循环，直至猜中该数，显示“恭喜！你猜中了！”。
示例1（“7”为输入）：
请输入你猜的数(0~9):7
恭喜！你猜中了！

示例2（5 6 9 7 为输入）：
请输入你猜的数(0~9):5
太小
请输入你猜的数(0~9):6
太小
请输入你猜的数(0~9):9
太大
请输入你猜的数(0~9):7
恭喜！你猜中了！
"""


num=7
while True:
    guess=int(input("请输入你猜的数(0~9):"))
    if guess==num:
        print('恭喜！你猜中了！')
        break
    elif guess>num:
        print('太大')
    else:
        print('太小')



"""
d=eval(input("请输入你猜的数(0~9):"))
a=7
while d!=a:

    if d<a:
        print('太小')
    elif d>a:
        print('太大')
    d=eval(input("请输入你猜的数(0~9):"))

print('恭喜！你猜中了！')

"""

"""
a=7
for g in range(0,9):
    d=eval(input("请输入你猜的数(0~9):"))
    if d==a:
        print('恭喜！你猜中了！')
        break
    elif d<a:
        print('太小')
    elif d>a:
        print('太大')
"""





"""
for g in range(1,9):
    d=int(input('请输入第%d次猜数的数值:'%g))
    if d==a:
        print('恭喜你，猜对了')
        break
    elif d<a:
        print('抱歉，你猜小了')
    elif d>a:
        print('抱歉，你猜大了')

"""
