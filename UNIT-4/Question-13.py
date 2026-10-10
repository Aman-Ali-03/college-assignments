with open("General.txt","r") as file:
    with open("Question-13.txt","w") as write:
        for line in file:
            if len(line)>1:
                write.write(line)