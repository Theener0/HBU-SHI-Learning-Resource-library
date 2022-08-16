"""	
题目内容：
输入扣税前工资金额，大于5000扣税3%，小于等于3000不扣税，3000和5000之间扣1%，输出到手的工资。
示例：
5000.0
4950.0
"""

gz=float(input())
if gz>5000:
    gz=gz*(1-0.03)
elif gz>3000:
    gz=gz*(1-0.01)
else:
    gz=gz
print(gz)

"""
x=eval(input())
if x>5000:
    x=x-x*0.03
elif x>3000:
    x=x-x*0.01
print(x)
"""

