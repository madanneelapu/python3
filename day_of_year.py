year = 2001
month = 4
day = 5

no_of_days = []

day_of_year = 0

leapyear = lambda year: year % 400 == 0 or year % 4 == 0 and year % 100 != 0

if leapyear(year):
    no_of_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    no_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for m in range(0,month-1):
    day_of_year += no_of_days[m]

day_of_year += day

print(day_of_year)
