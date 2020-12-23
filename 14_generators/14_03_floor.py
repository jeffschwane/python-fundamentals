'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

given_list = (x for x in range(1, 100000) if x % 1111 == 0)
for num in given_list:
    print(num // 1111)
