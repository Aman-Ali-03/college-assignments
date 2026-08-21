cost = 0
dis = 0
print("="*60)
print("\t SMARTCAMPUS UTILITY & ACCESS PASS GENERATOR")
print("="*60)
cat = int(input("Select User Category(1: Student,2: Faculty/Staff): "))
Pass = 0
discount = 0
if cat==1:
    subcat = input("Enter Sub-Category(UG / PG): ")
    if subcat=='UG'or'ug':
        cost += 500
        Pass = 500
    else:
        cost += 350
        Pass = 350
    cgpa = float(input("Enter Student CGPA(0.0 - 10.0): "))
    if cgpa>=8.5:
        cost = cost - (cost*0.2)
        discount = Pass*0.2
        dis = 20
    elif cgpa<8.50 and cgpa>7.5:
        cost = cost - (cost*0.1)
        discount = Pass*0.1
        dis = 10
else:
    subcat = int(input("Enter Sub-Catagory(1: Resident Faculty,2: Visiting/Guest Faculty): "))
    if subcat==1:
        cost += 800
        Pass = 800
    else:
        cost += 1200
        Pass = 1200
    service = int(input("Enter Year of Service: "))
    if service>10:
        cost = cost - (cost*0.15)
        discount=Pass*0.15
        dis = 15
parking_fee = 0
parking = int(input("Select Parking Permit (0: None,2: Two-Wheeler,4: Fout-Wheeler): "))
if parking==2:
    cost += 200
    parking_fee = 200
elif parking==4:
    cost += 600
    parking_fee = 600
elebill = 0
net = cost
fix=0
unit = int(input("Enter Monthly Electricity Consumption (in KWH): "))
if unit>500:
    elebill = (unit - 500)*10
    fix=250
    elebill += (300+1000+1500+fix)
    cost += elebill
elif unit>300:
    elebill = (unit - 300)*7.50
    fix=150
    elebill += (1000+300+fix)
    cost += elebill
elif unit>100:
    elebill = (unit - 100)*5
    fix = 100
    elebill += (300+fix)
    cost += elebill
else:
    elebill = unit*3
    fix = 50
    elebill += fix
    cost += elebill
print('-'*60)
print("CALCULATED INVOICE BREAKDOWN")
print('-'*60)
print(f"Base Access Pass Fee   :₹{Pass}")
print(f"Merit Discount ({dis}%)   :-₹{discount}")
print(f"Parking Fee ({parking}-Wheeler)   :₹{parking_fee}")
if cat==1 and parking==4:
    net+=150
    cost += 150
    print("Student Peak Surcharge   :150")
print(f"Net Pass & Parking Total   :₹{net}")
print("-"*60)
print(f"Electricity Bill({unit} kWh) :₹{elebill} ",end="")
print(f"(Slab calculate + Fixed Charge {fix})")
print("-"*60)
print(f"TOTAL MONTHLY PAYABLE   :₹{cost}")
print("="*60)