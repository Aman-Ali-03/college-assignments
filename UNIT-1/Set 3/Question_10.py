# Create two complex variables: c1 = 6 + 9j, c2 = 4 - 7j. Write a program to:
# Add the two complex numbers, Multiply them, Find the magnitude (absolute
# value) of each complex number, Print the data type of each result, Print the
# memory address of both variables.
import math
c1 = 6+9j
c2 = 4-7j
c1r = c1.real
c1i = c1.imag
c2r = c2.real
c2i = c2.imag
add = c1 + c2
c1m = abs(math.sqrt(pow(c1r,2)+pow(c1i,2)))
c2m = abs(math.sqrt(pow(c2r,2)+pow(c2i,2)))
print("Addition: ",add,type(add))
print("Multiply: ",c1*c2,type(c1*c2))
print("Magnitude of c1: ",c1m,type(c1m))
print("Magnitude of c2: ",c2m,type(c2m))
print(id(c1))
print(id(c2))