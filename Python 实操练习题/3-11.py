"""
题目内容：
输入一个三位数的整数，拆分该三位数，分别输出百位，十位和个位.

示例（只有“789”为输入）：
请输入一个三位数的整数:789
百位:7
十位:8
个位:9
"""

"""
a=input("请输入一个三位数的整数:")
a1=list(a)
a1= [int(i) for i in a1] 
print("百位:",a1[0],sep='')
print("十位:",a1[1],sep='')
print("个位:",a1[2],sep='')
"""

from math import *
x=int(input("请输入一个三位数的整数:"))
bw=x//100
sw=x//10%10
gw=x%10
print("百位:%d\n十位:%d\n个位:%d"%(bw,sw,gw))
