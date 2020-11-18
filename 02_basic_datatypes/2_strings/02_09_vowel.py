'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

str = input('Enter some words: ')
#print(str.count('a')+str.count('e')+str.count('i')+str.count('o')+str.count('u'))
for vowel in ['a','e','i','o','u']:
    print(f'{vowel} = {str.count(vowel)}')
