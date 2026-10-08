with open("Question-01.txt","r") as file:
    print(file.read(10))
    file.seek(0)
    print(file.read())