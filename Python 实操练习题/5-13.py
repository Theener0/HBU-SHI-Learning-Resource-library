"""
	
题目内容：
输入两个整数，将它们的值互换。

示例：
请输入第一个整数：5
请输入第二个整数：6
(6, 5)
 请注意，函数调用必须按如下所示编写（给定部分）：
a=int(input("请输入第一个整数："))
b=int(input("请输入第二个整数："))
print(change(a,b))

请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。
"""

def change(a,b):
    c=a
    a=b
    b=c
    return a,b
