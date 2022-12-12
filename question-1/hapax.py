#import regular expressions module which is a sequence of characters that forms a search pattern
import re

def hapax(filename):
    #opens the file name and in this case it is book.txt
    file = open(filename)
    #using the re.findall function to return a list containing all matches
    words = re.findall('\w+', file.read().lower())
    #ignores the capitalization
    freqs = {key: 0 for key in words}
    for word in words:
        #increment the count for that word
        freqs[word] += 1
    for word in freqs:
        #if the word has a count of one then it is hapax and will be put in the list
        if freqs[word] == 1:
            print (word)


hapax('question-1/book.txt')