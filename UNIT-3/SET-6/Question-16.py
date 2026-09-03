# Student Marks Program: Create a program using separate functions: input_marks(),
# calculate_total(), calculate_average(), display_result()
# Program should accept marks of 5 subjects & display total, average and result.

def input_marks():
    marks=[]
    for i in range(5):
        marks.append(int(input('Enter your number: ')))
    display_result(marks)
def calculate_total(marks):
    return sum(marks)
def calculate_average(marks):
    return (sum(marks)/len(marks))
def display_result(marks):
    print(f"Total Marks :{calculate_total(marks)}")
    print(f"Average Marks :{calculate_average(marks)}")
    print(f"Result :{'pass' if calculate_total(marks)>200 else 'Fail'}")
input_marks()