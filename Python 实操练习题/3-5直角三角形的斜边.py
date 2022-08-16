"""
从键盘上输入直角三角形的两个直边，求其斜边长并输出（保留两位小数）。
例（前2行为输入，第三行为输出）：
3.3
4.4
5.50
"""


from math import *
a=float(input('请输入直角边1:'))
b=float(input('请输入直角边2:'))
c=sqrt(a*a+b*b)
print("%.2f" % c)