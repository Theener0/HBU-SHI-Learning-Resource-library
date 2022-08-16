"""
编写函数，计算三门课程总分和平均值。
示例：
请输入数学成绩:77
请输入英语成绩:88
请输入语文成绩:90
成绩总和:255,平均成绩:85.00
 请注意，函数调用必须按如下所示编写（给定部分）：
math=int(input("请输入数学成绩:"))
eng=int(input("请输入英语成绩:"))
chinese=int(input("请输入语文成绩:"))
sum,avg=grade(math,eng,chinese)
print("成绩总和:%d,平均成绩:%.2f"%(sum,avg))

请将调试好的程序源代码（除已经“给定部分”的其余部分）复制到以下文本框，然后再点击“提交”按钮。  
"""

def grade(math,eng,chinese):
    sum=math+eng+chinese
    avg=sum/3
    return sum,avg