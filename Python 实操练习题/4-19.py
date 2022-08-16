"""
打印九九乘法口诀表，两个口诀之间用空格间隔。
"""

for i in range(1,10):
    a=''
    for j in range(1,i + 1):
        a+=str(j)+'*'+str(i)+'='+str(i*j)+' '   
    print(a)

"""
for i in range(1,10):
    for j in range(1,i + 1):
        print('{0}*{1}={2}'.format(j,i,i*j),end=' ')   
    print('')
"""

                                        			  																												  
