with open("General.txt","r") as reader:
    with open("Question-08.txt","a") as writer:
        for lines in reader:
            writer.write(lines.upper())