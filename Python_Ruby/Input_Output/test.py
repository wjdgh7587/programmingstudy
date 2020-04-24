ID = input("Put your ID\n")
Password = input("Put your Password\n")

print("\nDear "+ID+" your account has made\n")
print("Your password nubmer is "+Password+"\n")

login_str = input("Do you want to login(Yes/No)\n")
if "Yes"==login_str:
    yourId = input("Put your ID\n")
    if yourId == ID:
        yourPassword = input("Puy your PASSWORD\n")
        if yourPassword == Password:
            print("Welcome "+ID)
        else:
            print("Your password is wrong!\n")
    else:
        print("This ID does not exist\n")
else:
    print("Good bye")                 
        