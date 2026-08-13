# 12.Input three numbers. Check whether: The first
# number is greater than the second and The third
# number is greater than the first. Display the result.

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: ")) 

if a>b and a>c:
    print("Greatest no. : ",a)
elif b>a and b>c:
    print("Greatest no. : ",b)
else:
    print("Greatest no. : ",c)