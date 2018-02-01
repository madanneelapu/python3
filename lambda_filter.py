#filter method

def isodd(n):
    return n%2 == 1


nums = [12,54,89,75,64,58,23]

onums = filter(isodd, nums) #passing function as a parameter

for n in onums:
    print(n)


print()
#using filter method with lambda

enums = filter(lambda n: n%2 == 0,nums)

for n in enums:
    print(n)