"""
某人体重50kg，假设体重以每年2%的速度增长，编写程序输出未来10年此人的体重状况。
输出按如下格式（体重保留2位小数）：
1 years later:51.00
2 years later:52.02
3 years later:53.06
......
"""


from math import *
w = 50
for y in range(1,11):
    w=w*1.02 
    print("%d years later:%.2f"%(y,w))

"""
weighten = 50
for i in range(1,11):
    weighten=weighten+weighten*0.02
    print("%d years later:"%i,"{:.2f}".format(weighten),sep='')
"""







"""
import math as m

now = 50
num = 1.2
sum = now + num

for i in range(9):
    sum = sum + num
    print("%d years later:"%i,m.floor(sum))
"""