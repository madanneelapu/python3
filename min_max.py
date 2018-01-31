#take 10 numbers and print the minimum and maximum of them
for i in range (0,4):
    num = int(input("Enter a number: "))
    if i == 0:
        min,max = num,num
    elif num < min:
        min=num
    else:
        max=num




print(min)
print(max)
