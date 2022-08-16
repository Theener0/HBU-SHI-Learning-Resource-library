"""
题目内容：
利用下图公式计算e的近似值，要求最后一项的值小于10的-6次方即可。
最后输出e的近似值。

"""

from math import *

e=1
n=1
s=1
while (s>1.0E-6):
    s=s/n
    e+=s
    n=n+1

print(e)

"""
sum,tmp = 1,1
for i in range(1,20):
    tmp*=i
    sum += 1/tmp
print("e的近似值（精度为10**-6）为%.6f"%sum)
"""

"""

sum,tmp = 1,1
for i in range(1,20):
    tmp*=i
    sum += 1/tmp
print("e=%.6f"%sum)
"""

