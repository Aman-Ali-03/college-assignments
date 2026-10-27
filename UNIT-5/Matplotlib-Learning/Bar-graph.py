import matplotlib.pyplot as mpt

subjects = ["DS","DE","DSTL","COA","UHV","Python"]
marks = [45,48,37,45,39,43]

mpt.bar(subjects,marks,color="purple")
mpt.xlabel("Subject")
mpt.ylabel("Marks")
mpt.yticks(range(5,51,5))
mpt.grid(True)
mpt.show()