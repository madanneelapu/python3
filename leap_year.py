#Leap year program
year = input("Enter a Year: ")
year = int(year)
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")