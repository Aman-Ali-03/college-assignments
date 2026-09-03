# Write a function student_result(marks) that accepts a list of marks and returns:
# Total marks, Average marks, Highest marks, Lowest marks

def student_result(marks):
    return sum(marks),sum(marks)/len(marks),max(marks),min(marks)
markss = []
mark = ['Total marks = ','Average marks = ','Higest marks = ','Lowest marks = ']
no = int(input("Enter how many subject you have: "))
for i in range(no):
    markss.append(int(input("Enter your marks: ")))
ans = list(student_result(markss))
for i in range(4):
    print(mark[i],ans[i])