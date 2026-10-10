with open("General.txt","r") as first:
    with open("Question-08.txt","r") as second:
        with open("Question-14.txt","w") as writee:
            for line in first:
                writee.write(line)
                writee.write(second.readline())