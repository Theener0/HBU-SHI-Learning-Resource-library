"""
题目内容：
编写代码，有如下数字，
li = [1,2,3,4,5,6,7,8,8]
能组成多少个互不相同且不重复的数字的两位数。
"""

li=[1,2,3,4,5,6,7,8,8]
li2=[]
for a in li:
    for b in li:
        if a!=b:
            s=a*10+b
            if s not in li2:
                li2.append(s)

print(len(li2))


"""
n=0
li=[1,2,3,4,5,6,7,8,8]
lim=[]
for i in li:
    for j in li:
        x=10*i+j
        if lim.count(x)==0:
            lim.append(x)
n=len(lim)
print(n)
"""

"""
n=0
m=[]
li=[1,2,3,4,5,6,7,8,8]
for i in li:
    for j in li:
        if i != j:   #条件语句强调i不等于j
            n+=1    #每当i和j不相同的条件满足时会加一次n，可表示总共的数量
            num = '%i%i' %(i,j)
            m.append(num)  #可将所有互不相同的两位数做成字符串后添加成列表
        else:
            continue   #在语句块执行过程中跳出该次循环，执行下一次循环
            
print(n)   


"""