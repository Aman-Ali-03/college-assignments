with open("General.txt","r") as reader:
    with open("Question-07.txt","a") as writer:
        for lines in reader:
            if "python" in lines.lower():
                print("line has been writen.")
                writer.write(lines)