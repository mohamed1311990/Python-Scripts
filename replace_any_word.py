import re
mypath = input("enter your file full path: ")   # enter your file path
myfile = open(mypath, "r")                 # open it
read_myfile = myfile.read().lower()               # load it
myfile.close()

word_in_file = input("enter the word you want to replace in file: ")  # enter word want to replaced
new_word = input("enter your new word: ")                             # enter new word

for Word in read_myfile:
    read_myfile = read_myfile.replace(word_in_file, new_word)   # replacing operation

myfile = open(mypath, "w")        # open the file
myfile.write(read_myfile)         # insert new data in file
myfile.close()







