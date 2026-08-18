user = 'Aman'
pasword = 12307
User = input("Enter your user name: ")
if user==User:
    Pass = int(input("Enter your pasword."))
    if Pass == pasword:
        print("Login Succesful.")
    else:
        print("Wrong pasword.")
else:
    print("User not found.")