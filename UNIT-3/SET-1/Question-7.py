# Create two lists & combine them using `extend()`.Now, remove last element.

a = [1,2,3,4,5]
b = [6,7,8,9,10]

a.extend(b)

print(a)

a.pop()

print(a)