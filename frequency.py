""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
      curr_line += 1
    lines = lines[curr_line+1:]
    #print(lines)
    wordList = []

    for line in lines:
        if line in string.whitespace:
            lines.remove(line)
        else:
            words = line.split()
            for word in words:
                wordList.append(word)

#only uses first 10 lines of book

    for line in wordList[0:10]:
        index = 0
        for word in wordList:
            a = word.strip(string.punctuation)
            wordList[index] = a.lower()
            index += 1;
    return wordList


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    myDictionary = dict()
    for word in word_list:
        myDictionary[word] = myDictionary.get(word,0) + 1

    inverted = []
    for word,number in myDictionary.items():
        inverted.append((number,word))
    inverted.sort(reverse = True)
    return inverted[0:n-1]

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.whitespace)



print(get_top_n_words(get_word_list('pg32325.txt'),20))
