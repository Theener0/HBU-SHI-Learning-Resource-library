"""
求100～9910中，所有能被7和13整除的奇数，并使用print输出。
输出模式如下所示：
273
455
637
......
"""

from math import *
for i in range(100,9911):
    
    if i%7==0 and i%13==0 and i%2!=0:

        print(i)