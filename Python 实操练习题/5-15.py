"""
 	
题目内容：
输入两个正整数x,y(x<y)，计算[x,y]区间内所有整数之和。
示例：
请输入一个正整数x：2
请输入一个正整数y：100
5049

 请注意，函数调用必须按如下所示编写（给定部分）：
x=int(input("请输入一个正整数x："))
y=int(input("请输入一个正整数y："))
print(sum(x,y))


请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。
"""
def sum(x,y):
    sum=0
    for i in range(x,y+1):
        sum=i+sum
    return sum