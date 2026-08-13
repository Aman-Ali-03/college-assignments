# Swap two variables using tuple unpacking.

a = (1,2)

print("Before swaping")
print(a)

z,x = a
a = x,z
print("After Swaping")
print(a)