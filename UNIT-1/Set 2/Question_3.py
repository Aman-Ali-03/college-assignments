# Write a program to input two numbers and check:
# Are they equal?, Are they not equal?, Is the first
# number greater than the second?, Is the first
# number less than or equal to the second?

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if num1==num2:
    print("Both number are equal.")
else:
    if num1<num2:
        print("Second number is greater.")
    else:
        print("First number is greater.")