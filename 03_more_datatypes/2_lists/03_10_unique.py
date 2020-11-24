'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
from typing import Any, Union

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []
for index,value in enumerate(list_):
    list_.pop(index)
    if value not in list_:
        unique_list.append(value)
    list_.insert(index, value)
print(unique_list)