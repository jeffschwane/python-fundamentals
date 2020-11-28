'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(lst):
    maximum = max(lst)
    minimum = min(lst)
    average = sum(lst)/len(lst)
    summation = sum(lst)
    return maximum, minimum, average, summation

# call the function below here

print(stats(example_list))