"""
对列表x=[49,38,65,76,13,27]中偶数位置的数值求和，并使用print将结果输出。
第一个数49的位置为0，为偶数位置。
"""

from math import *
x=[49,38,65,76,13,27]
loc=0
sum=0
for i in x:
    if loc%2==0:
        sum+=i
    loc+=1
    
print(sum)

"""
x=[49,38,65,76,13,27]
sum=0
for i in range(0,6):
    if i==0 or i%2==0:
        sum=sum+x[i]
print(sum)
"""