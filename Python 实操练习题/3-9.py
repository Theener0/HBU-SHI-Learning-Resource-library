"""
从键盘上输入三角形的三条边，根据海伦公式求其面积并输出（保留三位小数）。
例（前三行为输入，最后一行为输出）：
2.2
3.3
4.4
3.515

"""
"""
import math
a=float(input())
b=float(input())
c=float(input())
p=(a+b+c)/2
s=p*(p-a)*(p-b)*(p-c)
S=math.sqrt(s)
print("%.3f"%S)
"""

from math import *
a=float(input())
b=float(input())
c=float(input())
p=(a+b+c)/2
S=sqrt((p-a)*(p-b)*(p-c))
print("%.3f"%S)

