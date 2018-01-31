#print words that are larger than 5 characters
st = "Python is a wonderful language. It is used for all purposes!"

words=[]

for w in st.split(" "):
    if len(w) > 5:
        words.append(w.strip(".!").upper()) #removing trailing . and ! characters. Converting to uppercase

for w in sorted(words): # sorted view of the list
    print(w)