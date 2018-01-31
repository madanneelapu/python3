nums = [102,33,11,23,30,98,90,15,833]

squares = []

for n in nums:
    squares.append(n * n)

print(squares)


# list comprehension
sqrs = [n * n for n in nums]
print(sqrs)