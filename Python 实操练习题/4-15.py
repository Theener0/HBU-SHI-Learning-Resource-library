
"""
从键盘上输入n，求n!并输出。
示例（只有第一行的“5”为输入）：
请输入n:5
5 != 120
"""

"""
i=int(input("请输入n:"))
s=1
for j in range(1,i+1):
    s=s*j
print(i,"!=",s)
"""

from math import *
n=int(input("请输入n:"))
s=1
for i in range(1,n+1):
    s=s*i
print(n,"!=",s)