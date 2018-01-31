#print number and square of 10 random numbers V2

import random

sq = {}

while len(sq) < 10:
    n = random.randint(1,100)
    sq[n] = n * n

for num,square in sq.items():
    print("%3d %6d" % (num,square))

print("No. of entries",len(sq))