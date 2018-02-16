import re

re1 = re.compile("[a-z]+")
match1 = re1.match("ab1 def 123 ghi 456")

if match1:
    print("Matched")
else:
    print("No match")

print()

match2 = re.match("[a-z]+", "ab1 def 123 ghi 456")

if match2:
    print("Matched")
else:
    print("No match")

print()

match3 = re.match("^[0-9]{6}$", "123456")

if match3:
    print("Matched")
else:
    print("No match")

print()

match4 = re.search("[0-9]+", "abc 123 456 bdec 963 789")

if match4:
    print("Matched")
    print(match4.span())

else:
    print("No match")

print()

match5 = re.match("[\w]+","213 sdsg 456s sfsff87s sgs")
if match5:
    print("Matched")
else:
    print("No match")