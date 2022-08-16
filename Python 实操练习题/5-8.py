"""
	
题目内容：
输入两个整数，输出其最大值。
示例（前两行为输入）：
1
2
2
 请注意，函数调用必须按如下所示编写（给定部分）：
a=int(input())
b=int(input())
print(find_max(a,b))
"""

def find_max(a,b):
    if a <= b:
        a=b
    return a
