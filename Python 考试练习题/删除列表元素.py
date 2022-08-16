"""
编写函数，从列表x中删除一个值a的元素，返回新的列表x。

测试用例:  (第1、2行为输入提示语及键盘输入值，第3行为输出结果)
请输入列表x:[1,2,3]  
请输入要移除的元素a:2
[1, 3]

请注意，main(函数或函数调用必须按如下所示编写:
x=eval(input("请输入列表x:"))
a=eval(input("请输入要移除的元素a:"))  
print(myremove(x,a))

"""

def myremove(x,a):
    num=x.count(a)
    for i in range(1,num+1):
        x.remove(a)
    return x

x=eval(input("请输入列表x:"))
a=eval(input("请输入要移除的元素a:"))  
print(myremove(x,a))