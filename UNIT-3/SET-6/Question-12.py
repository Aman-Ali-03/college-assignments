# 12.Write a function print_table(n) that prints the multiplication table of n.

def print_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
num = int(input("Enter your number to print the table: "))
print_table(num)