'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
entry = ""
entry = int(input("Enter a number between 1 and 1,000,000,000: "))
if entry%3 == 0:
    print(f"{entry} is divisible by 3.")
    print(entry/3)
