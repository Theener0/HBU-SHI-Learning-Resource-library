"""
 	
题目内容：
输入学生的分数score（提示信息为：“请输入学生分数:”），输出成绩等级。
其中分数大于或等于90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

示例1（只有“97”为输入）：
请输入学生分数:97
成绩等级为: A
"""

"""
score=int(input("请输入学生分数:"))
if score>=90:
    print("成绩等级为: A")
elif score>=60:
    print("成绩等级为: B")
else:
    print("成绩等级为: C")
"""

score=int(input("请输入学生分数:"))
if score>=90:
    grade='A'
elif score>=60:
    grade='B'
else:
    grade='C'
print("成绩等级为:",grade)  #print("成绩等级为:"+grade)