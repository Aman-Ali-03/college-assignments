# to accept 10 numbers from the user and count how many are positive, negative, and zero using a
# loop and conditional statements.

positive = 0
negative = 0
zero = 0
for i in range(0,10):
    n=int(input("Enter you number: "))
    if n>0:
        positive+=1
    elif n<0:
        negative+=1
    else:
        zero+=1
print("Positive =", positive)
print("Negative =: ",negative)
print("Zero =",zero)