import re

m1 = re.search("([a-zA-Z]+) (\d+) (\d+)", "Programmer 5000 50000")

print(m1.group(0))
print(m1.group(1))
print(m1.group(2))
print(m1.group(3))

print()

for g in m1.groups():
    print(g)

print()

print(m1.start(2))