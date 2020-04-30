id_list = ['naver', 'google', 'daum', 'git']
pswd_list = ['11', '22', '33', '44']

input_login = input("Do you want to login or create/delete(Yes/No/Cre/Del)\n")

if input_login == "Yes":
    input_id = input("Put your id\n")
    input_pswd = input("Put your pswd\n")
    
    for check_id in id_list:
        for check_pswd in pswd_list:
            if check_id == input_id and check_pswd == input_pswd:
                print("Hello "+input_id+"\n")
   
    print("You put wrong id or password\n")
    import sys
    sys.exit

elif input_login == "Cre":
    print("This is making id with password\n")
    cre_id = input("Put new id\n")
    cre_psw = input("Put new password\n")

    id_list.append(cre_id)
    pswd_list.append(cre_psw)

    print(id_list)
    print(pswd_list)

elif input_login == "Del":

    del_id = input("Put your id you want to delete\n")
    del_pswd = input("Put your password you want to delete\n")
 
    i=0
    for del_check_id in id_list:
        for del_check_pswd in pswd_list:
            if del_id == id_list[i] and del_pswd == pswd_list[i]:
                del(id_list[i])
                del(pswd_list[i])
        i=i+1    
    print(id_list)
    print(pswd_list)

else: 
    print("Good bye")    
