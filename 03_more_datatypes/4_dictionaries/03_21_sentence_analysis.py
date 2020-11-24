'''Write a script that takes a sentence from the user and returns:

the number of lower case letters
the number of uppercase letters
the number of punctuations characters
the total number of characters
Use a dictionary to store the count of each of the above.

Note: ignore all spaces.'''

import string
str = input("Enter a sentence: ")
count = {'lower':0,'upper':0,'punct':0,'char':0}
for letter in str:
    if letter.islower():
        count['lower'] +=1
    if letter.isupper():
        count['upper'] +=1
    if letter in string.punctuation:
        count['punct'] +=1
    if letter.isalpha():
        count['char']+=1
print(f"lowercase letters: {count['lower']}")
print(f"uppercase letters: {count['upper']}")
print(f"punctuation: {count['punct']}")
print(f"total characters: {count['char']}")


