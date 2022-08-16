"""
超市购物活动，购物金额>=300元提示用户“获得50元代金券” ，
金额在200-299元提示用户“获得20元代金券”， 
金额在100-199元提示用户“获得10元代金券”，
1-99元提示用户“无代金券”。
示例：
350
获得50元代金券
"""

from math import *
pay=float(input())
if pay>=300:
    print("获得50元代金券")
elif pay>=200:
    print("获得20元代金券")
elif pay>=100:
    print("获得10元代金券")
else:
    print("无代金券")

"""
x=eval(input())
if x>=300:
    print("获得50元代金券")
elif x>=200:
    print("获得20元代金券")
elif x>=100:
    print("获得10元代金券")
elif x>=1:
    print("无代金券")
"""
