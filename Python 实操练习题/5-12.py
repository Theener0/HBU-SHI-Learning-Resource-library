"""
	
题目内容：
编写函数，使用循环语句实现删除字符串s中的“*”功能。
示例（第1行为输入）：
This* is* a*book!
This is abook!
 请注意，函数调用必须按如下所示编写（给定部分）：
str=input()
print(delS(str))

请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。   
"""
def delS(str):
    strli=list(str)
    co=strli.count('*')
    for i in range(0,co):
        strli.remove("*")
    str="".join(strli)
    return str