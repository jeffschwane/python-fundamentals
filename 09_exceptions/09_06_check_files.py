'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
numbers = []
with open('/Users/jschw/OneDrive/Documents/Python Scripts/CodingNomads/Labs/09_exceptions/' + file_name, "r") as f_in:
    try:
        for line in f_in.readlines():
            line = line.rstrip()
            line = int(line)
            numbers.append(line)
        print(sum(numbers))
    except IOError:
        print("There was an IO error.")
    except ValueError:
        print("There was an unexpected value.")
