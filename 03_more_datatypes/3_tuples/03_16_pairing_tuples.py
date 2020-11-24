'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

str = input('Enter numbers: ')
lst = str.split()
lst = list(map(int, lst))
lst.sort()
if len(lst)%2 == 1:
    lst.append(0)
for i in range(0,len(lst)):
    if i%2 == 0:
        lst[i] = (lst[i],lst[i+1])
del lst[1::2]
for item in lst:
    print(item)