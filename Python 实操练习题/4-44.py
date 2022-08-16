"""	
题目内容：
鸡兔共30只，脚共90只，鸡兔各多少只？ 
输出鸡兔的数量，以空格间隔。例：“10 20”
"""
x=30
y=90
for i in range(0,25):
    for j in range(0,50):
        if i + j ==30 and i*4 + j*2 == 90:
            print(j,i)