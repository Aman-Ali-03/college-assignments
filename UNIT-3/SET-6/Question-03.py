# Write a function is_even(n) that returns True if the number is even, otherwise False.

def is_even(n):
    if n%2==0:
        return True
    return False

num = int(input("Enter your number: "))
print(f"Number is even: {is_even(num)}")