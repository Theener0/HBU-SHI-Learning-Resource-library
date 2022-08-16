"""
编写程序，解一元二次方程 ax^2+bx+c=0。
用户输入系数 a,b,c（提示信息分别为：“请输入a:”、“请输入b:”、“请输入c:”），
如果有实根，计算并输出实根，否则输出“无实根”。
"""

from math import*
a=float(input("请输入a:"))
b=float(input("请输人b:"))
c=float(input("请输人c:"))
delta=b*b-4*a*c
if(delta>=0):
    delta=sqrt(delta)
    x1=(-b+delta)/(2*a)
    x2=(-b-delta)/(2*a)
    print("两个实根分别为:",x1,x2)

else:
    print("无实根")
