# Write a function calculate(a, b) that returns the sum, difference, product, and
# division of two numbers.

def calculate(a,b):
    return a+b,a-b,a*b,a/b
operation = ['Sum = ','Difference = ','Multiply = ','Division = ']
first = int(input('Enter your first number: '))
second = int(input('Enter your second number: '))
ans = list(calculate(first,second))
for i in range(4):
    print(operation[i],ans[i])