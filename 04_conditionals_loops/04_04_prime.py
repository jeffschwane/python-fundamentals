'''
Print out every prime number between 1 and 100.

'''

for num in list(range(2,101)):
    prime = True
    for div in list(range(2,101)):
        if div == num:
            continue
        if num % div == 0:
            prime = False
    if prime == True:
        print(num)
