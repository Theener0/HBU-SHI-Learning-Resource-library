"""
题目内容：
求1-2+3-4+5 ... 99所有数的和。
"""
sum = 0
for i in range(1,100):
    if i%2==1:
        sum = sum + i
    else:
        sum = sum - i
print(sum)
