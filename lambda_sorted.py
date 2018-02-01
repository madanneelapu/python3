names = ['Bill Gates', 'Larray Ellison', 'Micheal Dell', 'Jeff Bezzos', 'Larry Page', 'Steve Jobs']


def length(s):
    return len(s)


def last_name(s):
    return s.split()[-1]  # splits the string with space and returns a list; -1 means the last item of the list


print("--Sorted By default--")
for s in sorted(names):
    print(s)

print("--Sorted By Length of the Name--")
# sorting by length of the name.
# the parameter 'key' takes a method which must return a value on which the sorting is to be based upon
for s in sorted(names, key=length):
    print(s)

print("--Sorted By Last Name--")
for s in sorted(names, key=last_name):
    print(s)


print("--Sorted By Last Name using Lambda--")
for s in sorted(names, key = lambda s: s.split()[-1]):
    print(s)