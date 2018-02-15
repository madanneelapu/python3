# Print the data in a file with line numbers
try:
    with open("names.txt", "r") as f: # try with resources kind of stuff. opening file in read mode
        lineno = 1
        for line in f.readlines(): # returns list of all lines from file
            print(lineno, line, end="")  # end is set to empty because, new line gets appended.
            lineno += 1

except:
    print("File not found")
