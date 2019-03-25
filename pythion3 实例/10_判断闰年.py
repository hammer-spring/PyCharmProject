'''
year = int(input("请输入一个年份："))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))
'''
import calendar

year = int(input("请输入年份："))
check_year=calendar.isleap(year)
if check_year == True:
    print ("闰年")
else:
    print ("平年")