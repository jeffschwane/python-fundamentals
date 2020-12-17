'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the first 100 characters of any of the files contain the string "Prince".

'''

words = []
with open("/Users/jschw/OneDrive/Documents/Python Scripts/CodingNomads/Labs/09_exceptions/books/war_and_peace.txt", 'r', errors='replace') as f_in:
    try:
        for line in f_in.readlines():
            words.append(line)
    except UnicodeDecodeError:
        pass

print(words[0][0])

with open("/Users/jschw/OneDrive/Documents/Python Scripts/CodingNomads/Labs/09_exceptions/books/crime_and_punishment.txt", "w") as f_out:
    f_out.write("")

words = []
with open("/Users/jschw/OneDrive/Documents/Python Scripts/CodingNomads/Labs/09_exceptions/books/crime_and_punishment copy.txt", "r",  errors='replace') as f_in:
    try:
        for line in f_in.readlines():
            words.append(line)
    except UnicodeDecodeError:
        pass

print(words[0][0])

words = []
with open("/Users/jschw/OneDrive/Documents/Python Scripts/CodingNomads/Labs/09_exceptions/books/pride_and_prejudice.txt", "r",  errors='replace') as f_in:
    try:
        for line in f_in.readlines():
            words.append(line)
    except UnicodeDecodeError:
        pass

print(words[0][0])
