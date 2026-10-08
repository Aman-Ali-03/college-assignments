with open("General.txt","r") as file:
    print(file.readline(),end="")
    print(file.tell())
    print(file.readline(),end="")
    print(file.tell())
    print(file.readline(),end="")
    print(file.tell())