"""
统计 1 到 n的累加和，当和大于1000时结束累加，分两行输出累加和及n的值（即只输出2个数）。

"""
from math import *
n=1
sum=0

while True:
    sum+=n
    if sum>1000:
        break;
    n=n+1

print(sum)
print(n)


