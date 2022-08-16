"""
从键盘上输入n，求1-n之间所有奇数之和。
（1）输入：100  输出：2500
（2）输入：1  输出：1
"""


n=int(input())
sum=0
for i in range(1,n+1):
    if i%2==1:
        sum+=i

print(sum)


"""
n=eval(input())
sum=0
for i in range(1,n+1):
    if i%2==1:
        sum=i+sum

print(sum)

"""


    