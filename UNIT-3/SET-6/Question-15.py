# Write a function get_grade(marks) that returns the grade according to:
# 90–100 → A, 80–89 → B, 70–79 → C, 60–69 → D, Below 60 → F

def get_grade(marks):
    if marks<101 and marks>89:
        return 'A'
    elif marks<90 and marks>79:
        return 'B'
    elif marks<80 and marks>69:
        return 'C'
    elif marks<70 and marks>59:
        return 'D'
    return 'F'
marks = int(input('Enter your marks: '))
print(f"You got {get_grade(marks)} Grade.")