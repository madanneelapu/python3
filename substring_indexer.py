#print indexes of substring in a string
mainString = "this is fine. However that is not fine. isn't it??"
subString = "is"
start = 0
while start < len(mainString):
    indexOfSubString = mainString.find(subString,start)
    if indexOfSubString == -1:
        break
    print(indexOfSubString)
    start = start + indexOfSubString + len(subString)


print("")
# Solution-2
start = 0
while True:
    pos = mainString.find(subString,start)
    if pos == -1:
        break

    print(pos)
    start = pos +1