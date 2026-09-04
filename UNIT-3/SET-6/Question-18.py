# Electricity Bill: Create a program using functions: get_units(), calculate_bill(),
# display_bill()
# Calculate electricity bill based on units consumed.

def get_unit():
    unit = int(input('Enter your unit consume :'))
    display_bill(unit)
def calculate_bill(unit):
    if unit>500:
        elebill = (unit - 500)*10
        fix=250
        elebill += (300+1000+1500+fix)
    elif unit>300:
        elebill = (unit - 300)*7.50
        fix=150
        elebill += (1000+300+fix)
    elif unit>100:
        elebill = (unit - 100)*5
        fix = 100
        elebill += (300+fix)
    else:
        elebill = unit*3
        fix = 50
        elebill += fix
    return elebill
def display_bill(unit):
    print(f"Your payable amount is {calculate_bill(unit)}")
get_unit()