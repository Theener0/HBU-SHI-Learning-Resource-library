"""
	
题目内容：
输入一个正整数，输出其所有因子。

示例：
请输入整数a:6
1,2,3,6

 请注意，函数调用必须按如下所示编写（给定部分）：
a=int(input("请输入整数a:"))
find_factor(a)  

请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。  
"""
def find_factor(a):
    x=[]
    for i in range(1,a+1):
        if a%i==0:
            x.append(i)
    print(",".join(str(i) for i in x))      
    return None
