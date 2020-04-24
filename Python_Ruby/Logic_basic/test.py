input_id = input("Type your id pls\n")
input_pswd = input("Type your pswd pls\n")

real_id = "wjdgh7587"
real_password = "wjdgh"

print("Your Id is "+real_id+" and your password is "+real_password+"\n")

input_login = input("Do you wanna login?(Yes/No)\n")

if input_login == "Yes":
    check_id = input("Type your id\n")
    check_password = input("Type your password\n")
    if real_id == check_id and real_password == check_password:
        print("Hello you have succeed your login!")
        print("Welcome "+real_id)
    elif real_id ==check_id or real_password == check_password:
        print("Sorry you put wrong password or id")
else:
    print("Godd bye!")            


