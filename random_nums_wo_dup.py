# create 10 random numbers without duplicates

import random

randomNums = set()

while len(randomNums) < 10:
    randomNums.add(random.randint(100,200))
    
print(randomNums)