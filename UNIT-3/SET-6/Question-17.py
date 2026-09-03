# Simple Calculator: Organise a calculator program using separate functions: add(),
# subtract(), multiply(), divide()
# The main program should ask the user for two numbers and an operation.

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
first = int(input('Enter your first number: '))
second = int(input('Enter your second number: '))
operator = input('Enter your operator(+,-,*,/): ')
if operator=='+':
    print('Addition :',add(first,second))
elif operator=='-':
    print('Subractor :',subtract(first,second))
elif operator=='*':
    print('Multiply :',multiply(first,second))
elif operator=='/':
    print('Division :',divide(first,second))
else:
    print('Invalid Input')