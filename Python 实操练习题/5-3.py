"""
	
题目内容：
编写函数计算圆的周长与面积，其中π使用 from math import * 中的pi。
示例：
请输入圆的半径:1.2
周长为7.54，面积为4.52
 请注意，函数调用必须按如下所示编写（给定部分）：
r=float(input("请输入圆的半径:"))
cir,area=getCirAndArea(r)
print("周长为%.2f，面积为%.2f"%(cir,area))
"""


def getCirAndArea(r):
    from math import pi
    cir=2*pi*r
    area=pi*r**2
    return cir,area