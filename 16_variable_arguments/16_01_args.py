'''
Write a script with a function that demonstrates the use of *args.

'''


def my_funct(number, *args):
    return number + sum(args)


print(my_funct(5, 6, 7, 8))
