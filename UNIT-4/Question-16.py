counter = 0
sum = 0
with open("Question-16.txt","r") as file:
    for i in file:
        sum += int(i)
        counter += 1

print(f"Avg = {sum/counter}")