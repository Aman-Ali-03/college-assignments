# using nested loop to print the multiplication tables from 2 to 5, with each table containing multiples
# from 1 to 10. Use a conditional statement to display only the multiples that are divisible by 3.

for i in range(1,6):
    for j in range(1,11):
        if (i*j)%3==0:
            print(i," x ",j," = ",i*j) 