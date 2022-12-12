#opens the file
myText = open('question-2/text.txt', 'r')
lines = myText.readlines()
#list all the sentence boundaries
punctuation = ".","?","!"
starter = ["mr.", "mrs", "jr.","ms.", "i.e."]

for line in lines:
    #split sentences into words
    words = line.split()
    for word in words:
        if word.lower() in starter:
            print(word + " ", end='')
        elif word[-1] in punctuation:
            #will create a new line
            print(word + "\n", end='')
        else:
            print(word + " ", end='')