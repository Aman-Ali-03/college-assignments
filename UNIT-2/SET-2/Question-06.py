for i in range(2,7):
    for j in range(1,6):
        if i>j:
            print(j,end="")
    print()
print("\n")
for i in range(2,7):
    for j in range(1,6):
        if i>j:
            print("*",end="")
    print()
print("\n")
for i in range(1,6):
    for j in range(0,i):
        print(i,end="")
    print()

print("\n")
for i in range(0,5):
    for j in range(0,6):
        if j<5-i:
            print(" ",end='')
        else:
            print(j,"",end='')
    print()
print("\n")
for i in range(0,5):
    for j in range(0,5):
        if j<4-i:
            print(" ",end='')
        else :
            print(i+j-3,end=' ')
    print()