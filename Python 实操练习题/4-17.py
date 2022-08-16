"""
我校现有3万名学生，按年增长率0.5%计算，多少年后人数超过3.5万？
输出一个数即可。

"""


from math import *
num=3
year=0
while num<=3.5:
    year+=1
    num*=1.005  
    #print("year",year,num)

print(year)

"""
x=30000
y=0
while x<35000:
    y+=1
    x=x+x*0.005
print(y)
"""

