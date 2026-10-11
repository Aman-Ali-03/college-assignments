# Create a file containing student records in the format:
#  RollNo, Name, Marks
#  Read the file and display students who scored more than 75.

with open("Challenge-01.txt","r") as list_of_student:
    for students in list_of_student:
        student = students.split()
        if int(student[2]) > 75:
            print(f"{student[0]} score more then 75")