st = input("Enter String: ")
vowels = ["a","e","i","o","u"]
fst = filter(lambda s:s not in vowels, st)

for s in fst:
    print(s,end="")