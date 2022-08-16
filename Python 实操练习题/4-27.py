"""
题目内容：
求1-2+3-4+5 ... 99所有数的和。

输出：50
"""


from math import *
sum = 0
for i in range(1,100):   
    if i%2==0:
        sum-=i
    else:
        sum+=i

print(sum)

"""
start = 1
sum = 0
while start <100:
    temp = start % 2    
    if temp ==1:
        sum = sum + start
    else:
        sum = sum - start
    start += 1
print(sum)
"""
