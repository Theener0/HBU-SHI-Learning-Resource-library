"""
1~n的正整数的平方和 
题目内容：
输入提示：“请输入n:”
注意输入提示没有空格，冒号为半角符号。
示例（下列两行信息中只有第一行的“5”为输入）：
请输入n:5
55
"""

"""
n=eval(input("请输入n:"))
f=0
for i in range(1,n+1):
    f=f+i*i
print(f)
"""

from math import *
n=int(input("请输入n:"))
sum=0
for i in range(1,n+1):
    sum=sum+i*i
print(sum)

