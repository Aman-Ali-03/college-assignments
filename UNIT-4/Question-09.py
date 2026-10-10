with open("General.txt","r") as readfrom:
    with open("Question-09.txt","w") as file:
        for line in readfrom:
            file.write(line[::-1])