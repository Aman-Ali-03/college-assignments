# Write a program that: Takes an integer as input.
# Apply the following operations one by one: += 10, -
# = 5, *= 2, /= 3. Display the value after each
# operation.

num = int(input("Enter your number: "))
num +=10
num -=5
num *=2
num /=3
print("After all operation: ",num)