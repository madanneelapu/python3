#generate 10 random numbers

import random

nums = []

for i in range(1,11):
    nums.append(random.randint(100,200))

print(nums)