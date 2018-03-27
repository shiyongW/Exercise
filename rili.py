#!/usr/bin/python
import calendar;
#year=int(input('year:'))
#print(calendar.calendar(year));
cal=calendar.month(2018,3,4,2);
print(cal);

print("是否闰年：",calendar.isleap(2018));
print("返回当前每周起始日期：",calendar.firstweekday());

print(calendar.monthrange(2018,3));


c=2;
a=3;
c**=a;
print(c);
