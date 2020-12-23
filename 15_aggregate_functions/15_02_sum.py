'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''


def sum(input_list):
    """Takes in a list and returns the sum"""

    sum = 0
    for element in input_list:
        sum += element
    return sum


my_list = [1, 5, 7, 9]
print(sum(my_list))
