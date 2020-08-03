import datetime

s = "2020年9月3日"

s1 = s.split("年")
s2 = s1[1].split("月")
s3 = s2[1].split("日")
year = int(s1[0])
month = int(s2[0])
day = int(s3[0])

date1 = datetime.date(year,month,day)
date2 = datetime.date(year,1,1)
x= (date1-date2).days+1
print(x)
