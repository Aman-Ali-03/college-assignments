# Read a source file and create:  
# . one file containing lines shorter than 40 characters 
# . one file containing lines 40 characters or longer

with open("Challenge-04.txt","r") as file:
    with open("Challenge-04-less-40.txt","w") as less:
        with open("Challenge-04-greater-40.txt","w") as greater:
            for line in file:
                if len(line)<40:
                    less.write(line)
                else:
                    greater.write(line)

    