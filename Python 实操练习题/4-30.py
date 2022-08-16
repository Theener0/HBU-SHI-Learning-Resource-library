"""
题目：
求100-200之间不能被3和7整除的数
"""
"""
s=0
for i in range(100,201):
    if i%3==0 and i%7==0:
        continue
    else:
        s=s+i
print (s)
"""

from math import *
sum=0
for i in range(100,201):
    if i%7!=0 and i%3!=0 :
        sum += i
print(sum)

