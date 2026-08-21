num = int(input("Enter number to get the factorial of the given number: "))
sum = 1
for i in range(1,num+1):
    sum *= i
print(f"Factorial of {num} is {sum}")