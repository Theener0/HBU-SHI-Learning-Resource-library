"""
已知x,y满足如图所示公式，输入a,b，求x,y的值(保留2位小数)  。
例(第1行为输入a,第2行为输入b，第3行为输出x，第4行为输入出y):
1.5
3.3
1.60
1.70

2x-y=a  
x+y=b
"""

a=float(input())
b=float(input())
x=(a+b)/3
y=2*x-a
print("%.2f"%x)
print("%.2f"%y)

