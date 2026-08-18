unit = int(input("Enter your unit: "))
if unit<=100:
    print(unit*5)
elif unit<=300:
    print(((unit-100)*7+500))
else :
    print(((unit-300)*10+1900))
