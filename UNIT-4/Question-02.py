with open("Question-02.txt","r") as file:
    print(file.read(5))
    file.seek(9)
    print(file.read(10))