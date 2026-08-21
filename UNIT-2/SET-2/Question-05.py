base = int(input("Enter your base value: "))
power = int(input("Enter the power of the number: "))
value = 1
for i in range(1,power+1):
    value = value * base
print(value)