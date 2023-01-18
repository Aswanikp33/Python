text="This is a sample line of operated text is"
words={}
text=text.split(" ")
for word in text:
    if word in words:
        words[word]+=1
    else:
        words[word]=1
print(words)