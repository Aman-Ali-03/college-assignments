# Using the nested dictionary created in Question 9, print only:

# * Name of Student 2 * Branch of Student 3 * CGPA of Student 1

student = {
    1:{'Name':'Aman Ali','Branch':'CSE','Semester':'3rd','CGPA':8.64},
    2:{'Name':'Rehan Ali','Branch':'DS','Semester':'3rd','CGPA':7.9},
    3:{'Name':'Arshlan Malik','Branch':'EC','Semester':'3rd','CGPA':8.43}
}

print(student[2]['Name'])
print(student[3]['Branch'])
print(student[1]['CGPA'])