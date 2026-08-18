balance = 5000
pin = 2987
Pin = int(input("Enter your pin: "))
if pin==Pin:
    Balance = int(input("Enter your balance: "))
    if Balance <= balance:
        print("Withdraw succesful.")
    else :
        print("Insuficent Balance.")
else:
    print("Invalid pin.")