# 11.Write a function check_prime(n) that returns whether a number is prime or not.

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n%i==0:
            return False
    return True
num = int(input('Enter your number: '))
print(f"Number is prime : {check_prime(num)}")