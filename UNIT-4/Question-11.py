longest = ""
with open("General.txt","r") as file:
    for line in file:
        if len(longest)<len(line):
            longest = line

print(longest)