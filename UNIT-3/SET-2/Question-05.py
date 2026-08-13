# Convert a list into a tuple and a tuple into a list.

a = [1,2,3,4,5,6,7,8,9]

b = tuple(a)
print(a,type(a))
print("b=a")
print(b,type(b))

c = (9,8,7,6,5,4,3,2,1)
d = list(c)
print("\n")
print(c,type(c))
print("d=c")
print(d,type(d))