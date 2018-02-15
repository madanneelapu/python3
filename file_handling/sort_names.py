# print names in sorted order
# This program can give some unexpected results if there is no new line at the end of the names.txt file.
# This is because when readlines() method is called, it reads each line along with the corressponsing new line character.
# If we remove the new line character at the end, then it does not get that new line.
# so it would consider Larry page(with new line) and larry page (without new line) as two different strings.
try:
    with open("names.txt", "r") as f:
        lines = set()
        for line in f.readlines():
            lines.add(line.strip("\n"))  # removing the new line characters

        for line in lines:
            print(line)

except:
    print("File not found")
