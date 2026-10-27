import matplotlib.pyplot as mpt

car = ["Audi","BMW","Lambo","Honda","Suzuki"]
sales = [23,43,12,45,41]
sale = [23,13,14,15,12]
mpt.plot(car,sales,marker = "s")
mpt.plot(car,sale,marker = "d")
mpt.xlabel("Cars")
mpt.ylabel("Sale")
mpt.show()