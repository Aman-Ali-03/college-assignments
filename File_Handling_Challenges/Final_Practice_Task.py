# Build a Student File Management Program using file operations only. It should allow the user to: 
# 1. Add a student record. 
# 2. Display all records. 
# 3. Search for a student by roll number. 
# 4. Count the total number of students. 
# 5. Append new records without deleting old records. 
# 6. Store records permanently in a text file. 
# 7. Handle the case where the file does not exist. 
# 8. Use at least one of read(), readline(), readlines(), write(), writelines(), and seek().

def Add_Student():
    roll = int(input("Enter Student Roll no: "))
    name = input("Enter Student Name: ")
    marks = int(input("Enter Student Marks: "))
    with open("Student.txt","a") as writee:
        writee.write(str(roll)+" "+name+" "+str(marks)+"\n")

def Display():
    print("Roll No  Name  marks")
    with open("Student.txt","r") as file:
        for line in file:
            print(line)

def Search_Student():
    roll = int(input("Enter Student Roll No: "))
    with open("Student.txt","r") as file:
        for line in file:
            line = line.split()
            if roll == line[0]:
                print(line)

def count_student():
    with open("Student.txt","r") as file:
        lines = file.read()
    lines = lines.splitlines()
    print(f"{len(lines)} Student in file.")

while(1):
    print("="*28)
    print("1. Add Student.")
    print("2. Display All Student.")
    print("3. Search Student.")
    print("4. Total Number Of Student.")
    print("5. Exit.")
    print("="*28)
    choice = int(input("Enter Your Choice: "))
    if choice==1:
        Add_Student()
    elif choice  ==2:
        Display()
    elif choice == 3: 
        Search_Student()
    elif choice == 4:
        count_student()
    elif choice == 5:
        break
    else:
        print("Invalid Choice.")