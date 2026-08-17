# Create a nested dictionary to store details of three students. Each student should
# have: Name, Branch, Semester, CGPA
# Print the complete nested dictionary.

student = {
    1:{'Name':'Aman Ali','Branch':'CSE','Semester':'3rd','CGPA':8.64},
    2:{'Name':'Rehan Ali','Branch':'DS','Semester':'3rd','CGPA':7.9},
    3:{'Name':'Arshlan Malik','Branch':'EC','Semester':'3rd','CGPA':8.43}
}

for i in student:
    print(student[i])
