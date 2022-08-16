"""
用户输入一个购买玉米的重量(整数类型)，判断并计算购买费用，并输出结果。
要求:
1、如果购买玉米不足10公斤，则每公斤售价为11元;  
2、如果购买玉米在10-50公斤(含10和50公斤)，每公斤售价为9元。  
3、如果购买玉米超过50公斤，每公斤售价为7元。
以下测试用例(第一行为输入，第二行为输出)
测试用例1:  
9
99
测试用例2:  
10
90
测试用例2:  
51
357
"""

weighten=int(input())
if weighten>50:
    pay=weighten*7
elif 50>=weighten and weighten>=10:
    pay=weighten*9
else:
    pay=weighten*11
print (pay)