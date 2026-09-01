# to find the sum of all numbers between 1 and 100 that are divisible by both 3 and 5.
sum = 0
for i in range(1,101):
    if i%3==0 and i%5==0:
        sum+=i
print("Sum =",sum)