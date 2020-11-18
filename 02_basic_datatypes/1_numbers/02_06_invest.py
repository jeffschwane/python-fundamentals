'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

amount = int(input("Enter investment amount: "))
int_rt = int(input("Enter interest rate in percentage: "))
years = int(input("number of years to invest: "))
FV = amount*(1+int_rt/100)**years
print(FV)