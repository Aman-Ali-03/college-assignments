# Create variables: A = 245, B = 37, C = -128.75. Write a program to: Calculate
# A2 using pow(), Find the absolute value of C, Print the maximum and
# minimum among A, B, and abs(C), Calculate the average of all three
# numbers., Display every result with appropriate labels.

a = 245
b = 37
c = -128.75
d = abs(c)
avg = (a+b+c)/3
print("A2: ",pow(a,2))
print("Absolute: ",d)
print(f"Max a: {max(a)}")
print(f"Min a: {min(a)}")
print(f"Max a: {max(b)}")
print(f"Min a: {min(b)}")
print(f"Max a: {max(d)}")
print(f"Min a: {min(d)}")
print(f"Avg: {avg}")