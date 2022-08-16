
year=int(input('请输入年份:'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    e=1
    print("闰年判断结果是:",bool(e))
else:
    e=0
    print("闰年判断结果是:",bool(e))