"""
从键盘上输入一列表，舍弃列表中能够被3整除的数值。
示例(第一行为输入)：
[1,2,3,4,5,6,7]
19

"""

x=eval(input())
sum=0
for item in x:
    if item%3==0:
        pass
    else:
        sum+=item
print (sum)


"""
m=eval(input())
s=0
for i in m:
    if i%3!=0:
        s=s+i
print (s)
"""



