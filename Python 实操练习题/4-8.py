"""
一个球从一定高度（用户输入）自由落下，每次落地后反跳回原高度的一般后再落下，
求它第十次落地时，共经过多少米?第十次反弹多高？
要求:(1)球落下的高度由用户输入：提示"请输入球落下的高度:"
    (2)输出计算得到的结果

示例：
请输入球落下的高度:100
共经过距离299.609375米
第10次反弹0.097656米

提示：
输出可以采用下面方法：
print("共经过距离%f米"%S)
print("第10次反弹%f米"%Hn)
"""

from math import *
s=float(input("请输入球落下的高度:"))
h=s/2
for i in range(2,11):
    s+=2*h
    h=h/2

print("共经过距离%f米"%s)
print("第10次反弹%f米"%h)