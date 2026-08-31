fees = 0
total = 0
Parking_charge = 0
charge=0
discount = 0
electricity_bill=0
fixed_charge=0
run = 0
print('='*60)
print('\tSMARTCAMPUS UTILITY & ACCESS PASS GENERATOR')
print('='*60)
category = int(input('Select User Category (1: Student,2: Faculty/Staff): '))
if category==1:
    sub_category = input('Enter your Sub-Category (UG/PG)')
    if sub_category.lower() == 'ug':
        fees=500
        total+=500
    elif sub_category.lower() == 'pg':
        fees=350
        total+=350
    else:
        run=1
    if run==0:
        cgpa = float(input('Enter your cgpa: '))
        if cgpa>10 or cgpa<0:
            print('Invalid CGPA')
            run+=1
        elif cgpa>=8.5:
            total -= (fees*0.2)
            discount = 0.20
        elif cgpa>=7.5 and cgpa<8.5:
            total -= (fees*0.1)
            discount = 0.10
elif category==2:
    sub_categorie = int(input('Enter sub-category (1: Resident Faculty,2: Guest Faculty): '))
    if sub_categorie == 1:
        fees = 800
        total+=800
    elif sub_categorie == 2:
        fees = 1200
        total+=1200
    else:
        print('Invalid Sub-Category')
        run+=1
    if run==0:
        year = int(input('Enter your year of Services: '))
        if year<0:
            print('Invalid Year of Services')
            run+=1
        elif year>10:
            total-=(fees*0.15)
            discount=0.15
else:
    print('Invalid Category')
    run += 1
if run==0:
    Vehicle = int(input('Select Parking Permit (0: None,2: Two wheeler,4: Four wheeler): '))
    if Vehicle==2:
        Parking_charge+=200
        total+=200
    elif Vehicle==4:
        Parking_charge+=600
        total+=600
        if category==1:
            charge=150
            total+=150
    elif Vehicle==0:
        pass
    else:
        print("Invalid Parking Permit")
        run += 1
if run==0:
    unit=int(input('Enter Monthly Electricity Consumption (in KWh):'))
    if unit<0:
        print('Invalid Unit Consumption')
        run=1
    if run==0:
        if unit<101:
            electricity_bill += (unit*3+50)
            fixed_charge+=50
        elif unit>100 and unit<301:
            electricity_bill += ((unit-100)*5+300+150)
            fixed_charge+=100
        elif unit>300 and unit<501:
            electricity_bill += ((unit-300)*7.5+1300+300)
            fixed_charge+=150
        else :
            electricity_bill += ((unit-500)*10 + 2800+550)
            fixed_charge+=300
if run==0:
    print('Base Access Pass Fee\t:₹',fees)
    if discount!=0:
        print(f"Merit Discount ({discount*100}%)\t:-₹{fees*discount}")
    if Vehicle!=0:
        print(f"Parking Fee({Vehicle}-Wheeler)\t:₹{Parking_charge}")
    if Vehicle==4 and category==1:
        print(f"Student Peak Surcharge\t:₹150")
    print(f"Net Pass & Parking Total:₹{total}")
    print("-"*40)
    print(f"Electricity Bill ({unit}kWh):₹{electricity_bill} (Slab calculated + Fixed Charge ₹{fixed_charge})")
    print("-"*40)
    total = total + electricity_bill
    print(f"TOTAL MONTHLY PAYABLE\t:₹{total}")
    print("="*60)