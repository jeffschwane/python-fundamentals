'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

def hello_there(name):
    return f'Hello {name}'

def apples(n):
    return f'I have {n} apples.'

def sentence():
    name = input('Enter your name: ')
    n = int(input('How many apples do you have? '))
    return hello_there(name), apples(n)

print(sentence())