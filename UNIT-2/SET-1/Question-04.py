marks = int(input("Enter your marks in percentage: "))
if marks>100:
    print("Invalid marks.")
elif marks==100 or marks>=90:
    print("Grade : A")
elif marks<=89 or marks>=75:
    print("Grade : B")
elif marks<=74 or marks>=60:
    print("Grade : C")
elif marks<=59 or marks>=40:
    print("Grade : D")
else :
    print("Fail")