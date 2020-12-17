'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

numerator = input('Enter the number to be divided: ')
denominator = input('Enter the number to divide by: ')
try:
    print(int(numerator) / int(denominator))
except ValueError:
    print('You need to enter a number!')
except ZeroDivisionError:
    print('You cannot divide by zero!')
