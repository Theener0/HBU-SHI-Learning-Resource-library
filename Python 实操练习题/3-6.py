"""
写程序，用户输入一个列表和两个整数作为起始序号（输入时运行界面的提示信息见示例），然后输出列表中介于这两个起始序号之间的元素组成的子列表。例如用户输入[1,2,3,4,5]，起始序号输入2和5，则输出子列表[3,4,5]。---------在实训平台提交
示例：
      请输入一个列表的组成元素：[1,2,3,4,5]
请输入较小的起始值a：2
请输入较大的起始值b：5
输出：子列表为： [3, 4, 5]
提示： eval()函数可将输入的列表字符串转换为列表

"""

x=eval(input('请输入一个列表的组成元素：'))
a=int(input('请输入较小的起始值a：'))
b=int(input('请输入较大的起始值b：'))
y=x[a:b]
m=list(y)
print("子列表为:",m)