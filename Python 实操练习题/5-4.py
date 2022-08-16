"""
题目内容：
输入三个边长，判断其是否构成三角形。
示例1：
请输入边长a:1.1
请输入边长b:2.2
请输入边长c:3
yes

示例2：
请输入边长a:1.1
请输入边长b:2.2
请输入边长c:5
no
 请注意，函数调用必须按如下所示编写（给定部分）：
a=float(input("请输入边长a:"))
b=float(input("请输入边长b:"))
c=float(input("请输入边长c:"))
print(istriangle(a,b,c))
"""
def istriangle(a,b,c):                
    if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
        m="yes"  
    else:
        m="no"
    return m                  

a=float(input("请输入边长a:"))
b=float(input("请输入边长b:"))
c=float(input("请输入边长c:"))
print(istriangle(a,b,c))
