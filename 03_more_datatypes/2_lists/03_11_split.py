'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

str = input('Enter some words: ')
list_ = str.split()
counter = {}

#Iterate through list of words and build dictionary with keys as # of occurrences
for value in list_:
    counter[list_.count(value)] = value
maximum = max(counter.keys())
print(counter[maximum])
