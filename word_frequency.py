#take a list of numbers and print how many times each number is present in the list

nums = [10, 20, 30, 50, 10, 40, 30, 20, 80, 20]

d1 = {}

for n in nums:
    if n in d1:
        c = d1[n]
        c += 1
        d1[n] = c
    else:
        d1[n]=1

print(d1)