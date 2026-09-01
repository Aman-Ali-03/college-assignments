# to generate the multiplication tables from 1 to 5. For each table, display only those multiples that
# are even.

for i in range(1,6):
    for j in range(1,11):
        if (i*j)%2==0:
            print(i," x ",j," = ",i*j)