"""
输入一组整数，求其和及平均值。
示例（只有“[1,2,3,4,5]”为输入）：

请输入一组整数:[1,2,3,4,5]
和为: 15
平均值为: 3.0
"""

x=eval(input("请输入一组整数:"))
sum=0 
avg=0 
num=0 
for s in x:
    sum+=s
    num+=1
print("和为:",sum)
avg=sum/num
print("平均值为:",avg)

"""
x=eval(input("请输入一组整数:"))
s=sum(x)
print("和为:",s)
print("平均值为:",s/len(x))

"""

"""
x=list(input("请输入一组整数:"))
y=','
c=0
for e in x:
    if y==e:
        c+=1     
for i in range(c):
    x.remove(y)     
x.remove('[')
x.remove(']')
m=[int(i) for i in x]
s=sum(m)
d=s/len(m)
print("和为:",s)
print("平均值为:",d)
"""

"""
x=[10,20,30,40,50,60,70,80,90,100]#s输入一组数
sum=0 #初始化sum=0
for i in x:
    sum=sum+i#t通过for循环，把x中的元素依次加起来
    print(sum,sum/len(x))#输出和以及平均数，len(x）代表x数组的元素个数
"""

"""
x=int(input("请输入一组整数:"))
sum=0 
for i in x:
    sum=sum+i
    print("和为:",sum)
    print("平均值为:",sum/len(x))
"""
