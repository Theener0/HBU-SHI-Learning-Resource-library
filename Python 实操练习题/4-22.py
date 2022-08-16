"""
	
题目内容：
从键盘上循环输入正整数，判断是否为素数，直到输入0时结束。
示例（输入 5 6 0）：

输入正整数,0为结束:5
5 是素数
输入正整数,0为结束:6
6 不是素数
输入正整数,0为结束:0

"""
from math import *
n=int(input("输入正整数,0为结束:"))
while(n!=0):
    flag=1
    k=int(sqrt(n+1))
    for i in range(2,k+1):
        if  n%i==0:
            print(n,"不是素数")
            flag=0
            break
        
    if(flag==1):
        print(n,'是素数')
    
    
    n=int(input("输入正整数,0为结束:"))


"""
from math import sqrt
m=int(input("输入正整数,0为结束:"))
while(m!=0):
    if m==1:
        print("1 不是素数")
    else:
        k=int(sqrt(m+1))
        for i in range(2,k+1):
            if m%i==0:
                print(m,"不是素数")
            else:
                print(m,"是素数")
        m=int(input("输入正整数,0为结束:"))


"""


"""
n = int(input("please enter the number："))
for i in range(2, n):
  if n % i == 0:
    print(" %d is not a prime number！" % n)
    break
else:
  print(" %d is a prime number！" % n)

"""