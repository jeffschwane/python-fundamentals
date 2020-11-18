'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

print('PIG LATIN!')
str = input('Enter words to translate: ')
first = str[0]
print(str[1:]+first+'ay'
      )