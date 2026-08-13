# Create a copy of a list using `copy()` and print both lists.

a = [1,2,3,4,5,6]
b = []

print("Before copy: ")
print("a= ", a)
print("b= ", b)

b = a.copy()

print("After copy: ")
print("a= ", a)
print("b= ", b)