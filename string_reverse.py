#print a string in reverse
s = input("Enter a String: ")

for i in range(1,len(s)+1):
    print(s[-i],end="")

print("")

# Solution-2
r = s[::-1]
print(r)