"""
列表求和，舍弃被3整除的值 
从键盘上输入一列表，舍弃列表中能够被3整除的数值。
示例(第一行为输入)：
[1,2,3,4,5,6,7]
19
"""

m=[1,2,3,4,5,6,7]
for i in m:
    if  i % 3 == 0:
        m.remove(i)
print(sum(m))