'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

entry = int(input("Enter a number between 1 and 1,000,000,000: "))

num = 0
while num != entry:
    num += 1
print(num)