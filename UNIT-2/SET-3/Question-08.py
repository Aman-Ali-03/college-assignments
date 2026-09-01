# to print numbers from 1 to 20, but use continue to skip all numbers that are divisible by 3.

for i in range(1,21):
    if i%3==0:
        continue
    print(i)