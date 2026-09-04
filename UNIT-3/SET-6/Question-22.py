# 23. Function Calling Function
# Create the following functions:

# get_number()
# square()
# cube()
# display()

# get_number() should provide a number to square() and cube(), and display() should
# display the results.

def get_number():
    number = int(input('Enter your number: '))
    display(number)
def display(number):
    print(f"Your number :{number}")
    print(f"Square of your number :{square(number)}")
    print(f"Cube of your number :{cube(number)}")
def square(number):
    return number*number
def cube(number):
    return number*number*number
get_number()        