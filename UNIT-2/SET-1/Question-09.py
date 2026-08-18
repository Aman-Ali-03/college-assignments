a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Devide")
choice = int(input("Enter your first number: "))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print("Invalid Choice.")