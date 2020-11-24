'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

entry = int(input("Enter a number: "))
if entry > 0 and entry < 12:
    if entry == 1:
        print("January")
    elif entry == 2:
        print("February")
    elif entry == 3:
        print("March")
    elif entry == 4:
        print("April")
    elif entry == 5:
        print("May")
    elif entry == 6:
        print("June")
    elif entry == 7:
        print("July")
    elif entry == 8:
        print("August")
    elif entry == 9:
        print("September")
    elif entry == 10:
        print("October")
    elif entry == 11:
        print("November")
    elif entry == 12:
        print("December")
else:
    print("Other")