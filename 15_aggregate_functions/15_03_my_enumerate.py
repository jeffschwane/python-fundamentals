'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''


def my_enumerate(iter, start=0):
    """Accepts an iterable and a starting count value as arguments
    Send back a tuple with the current count value and the associated item from the iterable """

    i = start
    for element in iter:
        yield i, element
        i += 1


seasons = ["Spring", "Summer", "Fall", "Winter"]
print(list(my_enumerate(seasons, start=1)))
