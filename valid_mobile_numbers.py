#Take a list of mobile numbers and print only valied mobile numbers in ascending order

mobileNumbers = ["7894561230", "456898", "456789130", "3216549870", "as5d4a5", "789456asda"]
validMobileNumbers = []

for num in mobileNumbers:
    if num.isdigit() and len(num) == 10:
        validMobileNumbers.append(num)

for num in sorted(validMobileNumbers):
    print(num)
