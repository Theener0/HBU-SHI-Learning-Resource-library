x=[11,22,50,73,81,99,100]
k=0
y=1
for item in x:
    if item%3==0:
        y=item
        break
    k=k+1
if(y!=1):
    print('找到能被3整除的数',y,'它是第',k+1,'个数')
else:
    print('没有找到能被3整除的数')
