# Prompt the user for input. This takes input in String format
num = input("Enter a Number : ")

# num % 2 will fail because 'num' will be a string.
# int(num) converts the 'num' value to integer.

if int(num) % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("The End!")
print