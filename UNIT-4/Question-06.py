with open("General.txt","r") as file:
    for lines in file:
        print(file.tell())
        print(lines)
        print(file.tell())