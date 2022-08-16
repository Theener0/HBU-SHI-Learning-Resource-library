"""
输入一个列表，求所有列表值的和。
(1)输入：[1,2,3,4,5]   输出：15
 请注意，函数调用必须按如下所示编写（给定部分）：
x =eval(input())
print(mysum( x ))
"""
def mysum(v):                
    s = 0
    for i in v:
        s=s+i                     
    return s
x =eval(input())
print(mysum( x ))
