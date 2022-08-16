"""
输入一个18位的身份证号(字符串类型)
从该身份证号中切片输出该身份证号中的出生年月日。
例如：(第1行为输入，第2行为输出):
130423200001010009
2000年01月01日
"""
id =input('输入身份证号码：')

id_no =list(id)
year = ''.join(id_no[6:10])
month =''.join(id_no[10:12])
day = ''.join(id_no[12:14])

"""
year=int(year)
month=int(month)
day=int(day)
"""

#print('%d年%d月%d日'%(year,month,day))

print(year,'年',month,'月',day,'日',sep='')