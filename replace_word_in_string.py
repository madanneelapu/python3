#Accept a string and a word and replace the occurance of the word with *

st = input("Enter string: ")
word = input("Enter word: ")

newStr = ""

for w in st.split(" "):
    w = w.strip(".")
    if w == word:
        newStr += " * "
    else:
        newStr += w + " "

print(newStr)