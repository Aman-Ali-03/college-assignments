"""Swap the values of two variables using both the
  traditional method and Python's tuple unpacking.
"""

a = 3
b = 2
a1 = 5
a2 = 4
print("*************************************")
print("Before Swaping.")
print(a)
print(b)
print("*************************************")
temp = a 
a = b
b = temp
print("After swaping using third variable.")
print(a)
print(b)
print("*************************************")
print("Before swaping.")
print(a1)
print(a2)
a1 = a1+a2
a2 = a1-a2
a1 = a1-a2
print("*************************************")
print("After swaping Without third variable.")
print(a1)
print(a2)
print("*************************************")