'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

# lst = [x for x in range(5)]
gen = (x for x in range(5))
# print(lst)
print(gen)
for num in gen:
    print(num)
