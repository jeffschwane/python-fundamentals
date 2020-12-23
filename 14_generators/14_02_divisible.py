'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

given_list = (x for x in range(1, 100000) if x % 1111 == 0)
for num in given_list:
    print(num)
