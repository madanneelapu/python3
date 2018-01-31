#varying arguments
def  sum(*nums):
    total = 0
    for n in nums:
        total += n

    return total


print(sum(1))
print(sum(1,2,3,4,5))
print(sum(1,2,3,4,5,6,7,8,9))

print()


#arguments that are delcared after varying arguments must be accessed with name
def  sum2(*nums, start):
    total = start
    for n in nums:
        total += n

    return total


#print(sum2(1,2)) #doesn't work.
#print(sum2(start=5,1,2)) #doesn't work
print(sum2(1,2,start=5))

print()


#arguments that are delcared after varying arguments must be set to a default value
def  sum3(*nums, start=10):
    total = start
    for n in nums:
        total += n

    return total


print(sum3(1,2))#works now!

print()



