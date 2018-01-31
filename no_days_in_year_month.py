#Accept Year and month and display no. of days in that month
year = input("Enter a Year: ")
year = int(year)
month = input("Enter a Month:")
month = int(month)
if month == 2:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(29)
    else:
        print(28)
elif month in [1,3,5,7,8,10,12]:
    print(31)
else:
    print(30)
