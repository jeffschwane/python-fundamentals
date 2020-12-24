'''
Write a script with a function that demonstrates the use of **kwargs.

'''


def my_funct(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')


my_funct(living_room='tripod light', kitchen='light strip')
