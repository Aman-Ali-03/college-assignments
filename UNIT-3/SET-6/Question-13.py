# 13.Write a function sum_of_digits(n) that returns the sum of digits of a number.

def sum_of_digit(n):
    sum = 0
    while n!=0:
        sum += n%10
        n//=10
    return sum
digit = int(input("Enter your digits : "))
print(f"Sum of your digit is {sum_of_digit(digit)}")