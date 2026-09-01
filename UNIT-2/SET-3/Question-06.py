# using nested loops to print all pairs (i, j) where i and j range from 1 to 5, but display only those
# pairs whose sum is even.
print('{',end='')
for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2==0:
            print(f"({i},{j})",end=', ')
print("}")