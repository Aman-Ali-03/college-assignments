# Create a menu-driven program using functions:
# 1. Check Even/Odd
# 2. Check Prime
# 3. Find Factorial
# 4. Find Square
# 5. Exit
# Each operation must be implemented using a separate function.

def check_even_odd(n):
    if n%2==0:
         return True
    return False
def check_prime(n):
    if n <= 1:
            return False
    for i in range(2, int(n**0.5) + 1): 
        if n%i==0:
            return False
    return True
def find_factorial(n):
    fact=1
    for i in range(1,n+1):
         fact*=i
    return fact
def square(n):
     return square*square
exit=0
while (exit!=5):
    print('1. Check Even/Odd.')
    print('2. Find Factorial.')
    print('3. Check prime.')
    print('4. Find Square.')
    print('5. Exit.')
    exit = int(input('Choice your operation: '))
    if exit==1:
        number = int(input('Enter your number: '))
        print('='*30)
        print(f"Number is even :{check_even_odd(number)}")
        print('='*30)
    elif exit==2:
        number = int(input('Enter your number: ')) 
        print('='*30)
        print(f"Factorial of {number} is {find_factorial(number)}")
        print('='*30)
    elif exit==3:
         number = int(input('Enter your number: '))
         print('='*30)
         print(f"{number} is prime :{check_prime(number)}")
         print('='*30)
    elif exit==4:
         number = int(input('Enter your number: '))
         print('='*30)
         print(f"Square of {number} is {square(number)}")
         print('='*30)
     