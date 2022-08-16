"""
题目内容：
输入半径（运行界面提示：“ r :”），计算并输出圆的周长和面积（结果保留两位小数）。

示例（只有第1行中的“5”为输入）：
r:5
L:31.42
S:78.54

注：
（1）保留两位小数的方法一：print("S:{:.2f}".format(S))
（2）保留两位小数的方法一二：print("S:%.2f"%(S))
（3）其中的π使用 pi, 需要在程序前加一行：from math import *


r:5
L:31.42
S:78.54
"""

from math import *
r=float(input(' r :'))

C=2*r*pi
S=pi*r*r

r=int(r)

print('r:',r)
print('L:','{:.2f}'.format(C))
print('S:','{:.2f}'.format(S))