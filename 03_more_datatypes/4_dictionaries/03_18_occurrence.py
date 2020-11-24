'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

str = input('Enter some words: ')
list_ = list(str)
counter = {}

#Iterate through list of letters and build dictionary with keys as letters and values as # of occurences
for value in list_:
    counter[value] = list_.count(value)
print(counter)