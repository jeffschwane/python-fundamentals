'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

str1 = input('Enter some words: ')
str2 = input('Enter some more words: ')
str3 = input('Enter even more words: ')

for str in [str1,str2,str3]:
#    print(f'{len(str)}, {str}')
    if max(len(str1),len(str2),len(str3)) == len(str):
        print(str)

