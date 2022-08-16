"""
编写程序，用户输入一个三位数的整数，输出三位数的和
例如
（1）输入：146 输出：1+4+6=11
"""



n = int(input())
bw= n//100
sw=n//10%10
gw=n%10
sum=bw+sw+gw
print("%d+%d+%d=%d"%(bw,sw,gw,sum))


"""
m = eval(input())
a = int(m/100)
b = int((m-a*100)/10)
c = m % 10
print("%d+%d+%d=%d"%(a,b,c,a+b+c))

"""