'''
Write a script that demonstrates a try/except/else.

'''

list_ = ["hello world!"]
try:
    print(list_[1])
except IndexError:
    print("This is out of range of the iterable")
try:
    print(list_[0])
except IndexError:
    print("This is out of range of the iterable")
else:
    print("This is now in range")
