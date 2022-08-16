"""
 	
题目内容：
编写程序，实现分段函数计算，如表所示（见教材P147）。
补全程序：程序见教材P147
程序运行示例如下表所示(示例中只有第一行的“-5”为输入)：
Please input x:-5
0

"""

x= eval(input('Please input x:'))
#eval(x)计算x中有效表达式的值
if x<0 or x>=20:
    print(0)
elif 0<=x<5:
    print(x)
elif 5<=x<10:   
    print(3*x-5)
elif 10<=x<20:
    print(0.5*x-2)
