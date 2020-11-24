'''
Write a script that takes a tuple and turns it into a list.

'''

str = input('Enter values for a tuple, separated by commas: ')
tup = tuple(str.split(","))
print(list(tup))