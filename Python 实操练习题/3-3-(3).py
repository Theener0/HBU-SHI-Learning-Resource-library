"""
(5)现有三位同学参加了比赛,记录列表存储在names 中,

names=['li','zhang' 'wang', 'zhang','Ii','wang', 'li', 'wang', 'wang',

请统计每个学生参加赛的次数并记录到字典d中,结果如下:

{'li':3，'zhang':2,'wang': 4}

"""

names=["li","zhang","wang","zhang","li","wang","li","wang","wang"]

a=names.count("zhang")
b=names.count("wang")
c=names.count("li")

outnames=dict(li=c,zhang=a,wang=b)

outnames


