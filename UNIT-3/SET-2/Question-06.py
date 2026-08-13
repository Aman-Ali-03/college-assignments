# Perform tuple packing and unpacking for student details. Demonstrate
# extended unpacking.

a = 1,2,3,4,5,6
print("Tuple Packing")
print("a = 1,2,3,4,5,6")
print("a=",a,type(a))

z,x,c,v,b,n = a
print("Tuple Unpaking")
print("z,x,c,v,b,n = a")
print("z=",z)
print("x=",x)
print("c=",c)
print("v=",v)
print("b=",b)
print("n=",n)

q,*w,e = a
print("Tuple Extended unpacking")
print("q,*w,e = a")
print("q=",q)
print("w=",w)
print("e=",e)