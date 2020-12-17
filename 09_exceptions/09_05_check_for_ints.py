'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

data = False
while data == False:
    entry = input("Enter an integer: ")
    try:
        int(entry)
        print(f"You entered the integer {entry}")
        data = True
    except ValueError:
        print("Please enter an integer.")
