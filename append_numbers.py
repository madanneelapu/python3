#take numbers as long as the input is not zero and the current given number is >= previous number

cur_num=0
numbers = []

while True:
    num = input("Please enter a number: ")
    try:
        num = int(num)
        if num == 0:
            break

        if num >= cur_num:
            numbers.append(num)
            cur_num = num
    except ValueError:
        print("Invalid Number")


print(numbers)