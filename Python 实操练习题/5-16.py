"""
输入一个正整数，判断其是否为奇数，如果为奇数，输出“Yes!”，否则为“No!”。

示例：
请输入一个正整数x：56
No!
 请注意，函数调用必须按如下所示编写（给定部分）：
x=int(input("请输入一个正整数x："))
print(odd(x))
                

请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。
"""

def odd(x):
    if x%2 == 0:return 'No!'
    else:       return 'Yes!'