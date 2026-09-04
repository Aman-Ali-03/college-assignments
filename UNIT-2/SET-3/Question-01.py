#to print all even & odd numbers separately from 1 to 50 using a loop and conditional statements.
print('Odd    Even')
for i in range(1,51):
    if i%2!=0:
        print(i,end='\t')
    else:
        print(i)