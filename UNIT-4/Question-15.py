even = open("Question-15-Even.txt","a")
odd = open("Question-15-Odd.txt","a")
for i in range(1,100):
    if i%2==0:
        even.write(str(i))
        even.write("\n")
    else:
        odd.write(str(i))
        odd.write("\n")