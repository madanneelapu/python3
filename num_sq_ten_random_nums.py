#print number and square of 10 random numbers

import random

sq = {}

for n in range (1, 11):
    n = random.randint(1,100)
    sq[n] = n * n

for num,square in sq.items():
    print("%3d %6d" % (num,square))

print("No. of entries",len(sq))