# 14.Write a function count_numbers(numbers) that accepts a list and returns the number
# of: Positive numbers, Negative numbers, Zeros

def count_number(numbers):
    p=0
    n=0
    z=0
    for i in numbers:
        if i<0:
            n+=1
        elif i>0:
            p+=1
        else:
            z+=1
    return p,n,z
num = int(input("How many number you want to enter: "))
number = []
rep = ['Positive: ','Negative: ','Zero: ']
for i in range(num):
    number.append(int(input("Enter your number: ")))
ans = count_number(number)
for i in range(3):
    print(rep[i],ans[i])