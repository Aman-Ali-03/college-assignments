# Create a program that prints the file pointer after each of these operations: 
# read(5), readline(), read(10), seek(0), and readlines().  Generate  -Markden

with open("Challenge-04.txt","r") as read_from:
    read_from.read(5)
    print(read_from.tell())
    read_from.readline()
    print(read_from.tell())
    read_from.read(10)
    print(read_from.tell())
    read_from.seek(0)
    print(read_from.tell())
    read_from.readline()
    print(read_from.tell())
