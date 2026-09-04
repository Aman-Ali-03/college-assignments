# 21. Convert this program into functions
# Given: 
# name = input("Enter name: ")
# marks = []
# for i in range(5):
#   marks.append(int(input("Enter marks: ")))
# total = sum(marks)
# average = total / 5
# if average >= 40:
#   result = "Pass"
# else:
#   result = "Fail"
# print("Name:", name)
# print("Total:", total)
# print("Average:", average)
# print("Result:", result)

# Task: Divide this program into at least 4 meaningful functions.

def display(name,marks):
    print("Name: ",name)
    print("Total: ",total(marks))
    print("Average: ",average(marks))
    print("Result: ",result(marks))
def total(marks):
    return sum(marks)
def average(marks):
    return sum(marks)/5
def result(marks):
    if average(marks)>=40:
        return "Pass"
    return "Fail"

name = input("Enter name: ")
marks = []
for i in range(5):
    marks.append(int(input("Enter marks: ")))
display(name,marks)