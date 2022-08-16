"""
键盘上输入正整数n，计算并输出1+2+3+...+n 的值。
示例（只有“99”为输入）：
请输入n:99
4950
"""

"""
i=int(input("请输入n:"))
s=0
for j in range(1,i+1):
    s=s+j
print(s)
"""

from math import *
sum=0
n=int(input("请输入n:"))
for i in range(1,n+1):
    sum+=i
    i+=1
print(sum)