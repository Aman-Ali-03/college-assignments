# to check whether a given number is an Armstrong number or not using a loop and conditional
# statements.

number = int(input("Enter your number: "))
temp = number
check = 0
while number!=0:
    check = (check*10)+number%10
    number//=10
if temp==check:
    print("Enter number is armstrong number.")
else:
    print("Enter number is not a armstrong number.")