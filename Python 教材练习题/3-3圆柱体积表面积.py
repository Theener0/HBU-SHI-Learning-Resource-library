from math import *
r=float(input('请输入半径:'))
h=float(input('请输入高:'))
v=1/3*pi*r**2*h
s=pi*r*sqrt(r**2+h**2)+pi*r**2
print('体积:',v,'表面积:',s)
