"""
从键盘键入坐标x，y，判断其位于的象限。
示例：
请输入x坐标:
请输入y坐标:
位于第一象限

输出结果可能是：
位于原点
位于x轴
位于y轴
位于第一象限
位于第二象限
位于第三象限
位于第四象限
"""

x=int(input("请输入x坐标:"))
y=int(input("请输入y坐标:"))

if (x==0)and(y==0):
    print("位于原点")
elif (x==0):
    print("位于y轴")
elif (y==0):
    print("位于x轴")
elif (x>0)and(y>0):
    print("位于第一象限")
elif(x<0)and(y>0):
    print("位于第二象限")
elif(x<0)and(y<0):
    print("位于第三象限")
else:
    print("位于第四象限")
