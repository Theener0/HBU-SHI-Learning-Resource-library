"""
猴子吃桃子问题。
小猴在一天摘了若干个桃子，当天吃掉一半多一个；第二天接着吃了剩下的桃子的一半多一个；
以后每天都吃尚存桃子的一半零一个，到第n天早上要吃时只剩下一个了，问小猴那天共摘下了多少个桃子？

示例：
请输入n(n>=2):2
第一天的桃子数为： 4
 请注意，函数调用必须按如下所示编写（给定部分）：
n=int(input("请输入n(n>=2):"))
print("第一天的桃子数为：",peach(n)) 

请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。  
"""
def peach(n):
    x=1
    for i in range(1,n):
        x=x+1
        x=x*2
    return x