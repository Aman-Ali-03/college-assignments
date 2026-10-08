with open("General.txt","r") as file:
    print(file.read())
    file.seek(0)
    print(file.readline())