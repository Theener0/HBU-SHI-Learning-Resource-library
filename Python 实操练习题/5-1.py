"""
编写函数求出区间[x,y]内所有整数的和。

 请注意，函数调用必须按如下所示编写（给定部分）：
x=int(input())
y=int(input())
sum=mySum(x,y)
print(sum)

请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。                     
"""

def mySum(x,y):
    sum=0
    for i in range(x,y+1):
        sum=sum+i
    return sum
    


