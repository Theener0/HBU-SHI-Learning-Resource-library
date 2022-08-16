"""
题目内容：
从键盘上输入学生人数与学生成绩，统计及格人数与所有及格同学的平均成绩。
示例：
输入总人数:5
99
85
76
32
67
及格人数 4 人,平均成绩是 81.75
"""

x=[]
count=eval(input("输入总人数:"))

for i in range(1,count+1):
    num=eval(input())
    x.append(num)

sum=0 
n=0          
for item in x:
    if item>=60:
        n+=1
        sum+=item

print("及格人数",n,"人,平均成绩是",sum/n)
#print("及格人数 %d 人,平均成绩是 %.2f"%(n,sum/n))


"""
ch=[]
num=eval(input("输入总人数:"))
numji=0
for i in range(1,num+1):
    x=eval(input())
    if x>=60:
        numji+=1
        ch.append(x)

sum1=0              #sum1=sum(ch)
for j in ch:
    sum1=sum1+j

pj=sum1/numji
print("及格人数 %d 人,平均成绩是 %.2f"%(numji,pj))

"""

