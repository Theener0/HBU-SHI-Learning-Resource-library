""""
从键盘上输入一个列表，计算其中所有奇数的和并输出。
注：输入列表的语句可使用 x=eval(input())
下列示例中第1行为输入，第2行为输出。
示例1：
[1,2,3,4]
sum= 4

 示例2：
[2,4,6]
sum= 0
"""

x=eval(input())
sum=0
for i in x:
    if i%2==1:
        sum=i+sum

print("sum=",sum)