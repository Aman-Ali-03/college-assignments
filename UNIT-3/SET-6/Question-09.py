# Write a function reverse_number(n) that returns the reverse of a number.

def reverse_number(n):
    rev = 0
    while n!=0:
        rev = (rev*10)+n%10
        n//=10
    return rev
num = int(input('Enter your number : '))
print(f"Reverse of your number {reverse_number(num)}")