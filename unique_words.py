#Accept a string and display only unique words

s = "Hi I am Madan. I am learning python."
words=set()

for w in s.split(" "):
    words.add(w)
    
print(words)