"""
题目内容:
从键盘上输入圆锥体的底面半径与高，计算其体积与表面积(均保留2位小数)。  

输入:
5.0
6
输出:
V:157.08
S:201.22
圆锥体的底面半径为r，高为h
则体积:V=1tr2h3
L2=r2+h2，
表面积为:S=TrL+Tr  2

"""

from math import *  
r=float(input())  
h=float(input())  

V=1/3*pi*r**2*h  
L=sqrt(r**2+h**2)   #L=(r**2+h**2)**(1/2)
S=pi *r*L+pi*r**2

V=round(V,2)
S=round(S,2)

print("V:",V)
print("S:",S)