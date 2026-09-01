# that repeatedly accepts numbers from the user and calculates their sum. Terminate the loop using
# break when the user enters 0.

inpu = 1
sum = 0
while inpu!=0:
    inpu = int(input("Enter number(exit: 0): "))
    sum+=inpu
    print("sum = ",sum)