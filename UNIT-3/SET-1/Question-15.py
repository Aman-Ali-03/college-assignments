# Perform the following slicing operations on a list of numbers from 1 to 10:
# First 5 elements, Last 5 elements, Every second element, Reverse the list

a = [1,2,3,4,5,6,7,8,9,10]

f5 = a[0:5:1]
l5 = a[5:10:1]
Es = a[::2]
rl = a[::-1]

print(a)
print(f5)
print(l5)
print(Es)
print(rl)