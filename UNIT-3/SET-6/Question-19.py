# Shopping Bill: Create separate functions: input_items(), calculate_total(),
# calculate_discount(), generate_bill()
# The program should accept item prices and quantities and finally display the bill.

def input_items():
    item_price = int(input("Enter your item price: "))
    item_quantity = int(input("Enter your quantity"))
    generate_bill(item_price,item_quantity)
def calculate_total(price,quantity):
    return price*quantity
def calculate_discount(price,quantity):
    bill = calculate_total(price,quantity)
    if bill>2000:
        return bill*0.2
    return bill*0.1
def generate_bill(price,quantity):
    print(f"Your bill : {calculate_total(price,quantity)}")
    print(f"Your discount : {calculate_discount(price,quantity)}")
    print(f"Net bill : {calculate_total(price,quantity)-calculate_discount(price,quantity)}")
input_items()