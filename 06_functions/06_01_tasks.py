'''

Write a script that completes the following tasks.

'''


# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

def div4or7(n):
    if n % 4 == 0 or n % 7 == 0:
        return True
    else:
        return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

def div4and7(n):
    if n % 4 == 0 and n % 7 == 0:
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000

entry = int(input('Enter a number between 1 and 1,000,000,000: '))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables

output_1 = div4or7(entry)
output_2 = div4and7(entry)

# print your new variables to display the results

print(output_1)
print(output_2)
