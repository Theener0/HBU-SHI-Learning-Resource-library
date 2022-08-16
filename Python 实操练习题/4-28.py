"""
从键盘上输入n，计算1-n之间能够5整除的奇数之和。
（1）输入：5  输出：5
（2）输入：100  输出：500

"""
from math import *
n=int(input())
sum=0
for i in range(1,n+1):
    if i%5==0 and i%2==1:
        sum=sum+i

print(sum)

"""
n=eval(input())
sum=0
for i in range(1,n+1):
    if i%5==0 and i%2==1:
        sum=sum+i

print(sum)

"""