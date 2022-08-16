"""
输入一个列表，移除列表中的奇数。
示例：
[1,2,3,4,5]
2 4 
 请注意，函数调用必须按如下所示编写（给定部分）：
L=eval(input())
L1=remove_odd(L)
for x in L1:
   print(x,end=' ')

请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。      
"""


def remove_odd(L):
    Lnew=[]
    for i in L:
        if i%2==0:
            Lnew.append(i)
    return Lnew




"""
66分

def remove_odd(L):
    for i in L:
        if i%2==1:
            L.remove(i)
    return L
"""
