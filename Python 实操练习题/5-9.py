"""
题目内容：
输入一个列表，求列表中的最小值及该值在列表中的索引。
示例：
[2,23,3,-234,23,66]
列表中的最小值：-234，索引值：3
 请注意，函数调用必须按如下所示编写（给定部分）：
L=eval(input())
minL,loc=find_min(L)
print("列表中的最小值：%d，索引值：%d"%(minL,loc))

"""

def find_min(L):
    minL=min(L)
    loc=L.index(minL)
    return minL,loc