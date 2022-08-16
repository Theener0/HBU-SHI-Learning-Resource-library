"""
题目内容：
输入分数，如果分数>=90，则输出“优”;  
如果分数在80~89之间，则输出“良”;  
如果分数在70~79之间，则输出“中”；
如果分数在60~69之间，则输出“及格”；
如果分数小于60，则输出“你不及格！请注意补考通知！”；
如果输入的分数在[0,100]之外，提示“输入有误！”。

注意：输入和输出必须完全按照测试用例测试通过才满分
输入分数时，即score=input("score:")
输出时，即print("grade:",grade)
测试用例：
输入          输出
92            grade: 优
85            grade: 良
55            grade: 你不及格！请注意补考通知！
200          输入有误！

注：“！”为中文符号
"""

from math import *
s=input("score:")
if s.isnumeric()==True and 100>=int(s)>=0:
    s=int(s)
    if s>=90:grade="优"
    elif s>=80:grade="良"
    elif s>=70:grade="中"
    elif s>=60:grade="及格"
    else:grade="你不及格！请注意补考通知！"
    print("grade:",grade)
else:
    print("输入有误！")




"""
score=eval(input("score:"))
if score<=100 and score>=0:
    if score>=90:
        grade="优"
    elif score>=80:
        grade="良"
    elif score>=70:
        grade="中"
    elif score>=60:
        grade="及格"
    else:
        grade="你不及格！请注意补考通知！"
    print("grade:",grade)
else:
    print("输入有误！")
"""