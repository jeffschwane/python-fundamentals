'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

str = input("Enter two numbers: ")
lst = list(map(int,str.split()))
sum = 0
for num in list(range(lst[0],lst[1]+1)):
    sum += num
print(sum)