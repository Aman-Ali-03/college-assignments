# Number Analysis Program: Create a program using separate functions:
# input_number(), check_even_odd(), check_prime(), find_factorial(),
# display_result()
# The program should accept a number and display all the required results.
def input_number():
    num = int(input('Enter your number: '))
    display_result(num)
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
def display_result(num):
    print("Your number is ",num)
    print(f"{num} is even {check_even_odd(num)}")
    print(f"{num} is prime {check_prime(num)}")
    print(f"Factorial of {num} is {find_factorial(num)}")
input_number()