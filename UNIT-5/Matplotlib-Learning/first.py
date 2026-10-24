import matplotlib.pyplot as mpt

a = ["Math","English","Hindi","Science","Python","COA","Mecanical","Electrical","PPs","Physics"]
b = [10,20,30,40,50,60,70,80,90,100]

mpt.bar(a,b,color = "purple")
mpt.title("Result Analysics")
mpt.xlabel("Marks")
mpt.ylabel("Subjects")
mpt.yticks(range(10,101,10))
mpt.show()