# 4. Input the marks of a student in two subjects.
# - Print "Pass" if both marks are 35 or above.
# - Print "Eligible for Scholarship" if either mark is 90 or
# above.
# - Print whether the student has not failed using the not
# operator.

sub1 = int(input("Enter your first subject marks: "))
sub2 = int(input("Enter your second subject marks: "))

if sub1 and sub2 >=35:
    print("You pass the exam.")
else:
    print("you fail the exam.")
if sub1 and sub2 >=90:
    print("Eligible for Scholarship")       