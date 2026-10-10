shortest = ""
with open("General.txt","r") as file:
    for line in file:
        if len(line)<len(shortest):
            shortest = line

print(shortest)