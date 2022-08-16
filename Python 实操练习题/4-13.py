"""
有一分数序列：2/1,3/2,5/3,8/5,8/13，21/13...求出这个序列的前20项之和。
以字符串 2/1+3/2+5/3+8/5+13/8+21/13+……= result 的形式返回结果。要求结果保留2位小数。
"""

"""
a1=1
a2=2
s=0
for i in range(20):
    s+=a2/a1
    a1,a2=a2,a1+a2
print("%.2f" %s)
"""

from math import *
fz=2
fm=1
s=fz/fm
for i in range(2,21):
    t=fz
    fz=fz+fm
    fm=t
    s=s+fz/fm

print("%.2f" %s)

