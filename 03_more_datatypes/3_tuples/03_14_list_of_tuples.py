'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

str = input('Enter some words: ')
lst = str.split()
for index,word in enumerate(lst):
    lst[index] = tuple(word)
print(lst)