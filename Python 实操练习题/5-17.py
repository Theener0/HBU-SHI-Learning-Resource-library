"""
题目内容：
输入字符串，判断其长度是否大于或等于5。如果是输出“True”，否则输出“False”。
示例1：
请输入内容：HUE
False
 请注意，函数调用必须按如下所示编写（给定部分）：
content=input("请输入内容：")
print(lenJudge(content))

请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。    

"""
def lenJudge(content):
    contentl=list(content)
    conlen=len(contentl)
    if conlen>=5:return True
    else:       return False