"""
输入三个整数x,y,z,判断三个数的大小，按从大到小的顺序输出三个整数。
示例：
2
3
1
3>2>1
"""

"""
数组排序
"""

x = int(input())
y = int(input())
z = int(input())
if x<y:
    t=x
    x=y
    y=t

if x<z:
    t=x
    x=z
    z=t

if y<z:
    t=y
    y=z
    z=t

print("%d>%d>%d"%(x, y, z))



"""
x = int(input())
y = int(input())
z = int(input())
if y > x:
    if z > y:
        z, x = x, z
    else:
        if x > z:
            y, x  = x, y
        else:
            x, y, z = y, z, x
else:
    if z > x:
        x, y, z = z, x, y
    else:
        if z > y:
            z, y = y, z
print("%d>%d>%d"%(x, y, z))
"""