from datetime import date, time, datetime, timedelta

t = timedelta(days=10)  # time delta object for representing period

print(t)

cd = date.today()  # get current system date
print(cd)

d = cd + t  # add 10 days to date
print(d)

print(cd < d)  # date comparision

print(d.year, d.month, d.day)
