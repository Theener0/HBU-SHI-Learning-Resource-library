"""
求1-100之间所有偶数之和。
"""

from math import *
sum=0
for i in range(0,101):
    if (i%2==0):
        sum+=i
print(sum)



"""
for i in range(0,101,2):
    sum=sum+i
print(sum)
"""

"""
sum = 0
a = 0
while a <= 100:
    if a % 2 == 0:
        sum =sum + a
    a = a + 1
print(sum)


"""

