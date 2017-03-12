import string

wordList = ['girl.','icecream','--sdafojieea']

index = 0
for word in wordList:
    wordList[index] = word.strip(string.punctuation)
    print(word)
    index += 1;

print(wordList)
