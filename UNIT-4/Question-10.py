dictonary = dict()
with open("General.txt","r") as readfrom:
    for line in readfrom:
        word = line.split()
        for i in word:
            i = i.lower()
            if i in dictonary.keys():
                dictonary[i] += 1
            else:
                dictonary[i] = 1

for i in dictonary.keys():
    print(i," : ",dictonary[i])
        