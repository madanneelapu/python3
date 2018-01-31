nums = [102,33,11,23,30,98,90,15,833]

evens = []
odds = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print(evens)
print(odds)