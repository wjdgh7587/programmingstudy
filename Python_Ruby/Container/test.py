ID_list = ['wjdgh75874', 'wjdgh75872', 'wjdgh75873']
Pswd_list = ['11', '22', '33']

print("Hello sir, please follow the direction")

login_str = input("Do you want to login?(Yes/No)\n")

if login_str == "Yes":
	print("Follow the direction")
	check_id = input("Put your id\n")
	check_pswd = input("Puy your pswd\n")
	if check_id == ID_list[0] and check_pswd == Pswd_list[0]:
		print("Hello "+ID_list[0])
	elif check_id == ID_list[1] and check_pswd == Pswd_list[1]:
		print("Hello "+ID_list[1])
	elif check_id == ID_list[2] and check_pswd == Pswd_list[2]:
		print("Hello "+ID_list[2])
	
else:		
	commit_information = input("Do you want to delete your Id and pswd?(New/No)\n")
	if commit_information == "New":
		input_id = input("Put your New Id\n")
		input_pswd = input("Put your New Password\n")

		ID_list.append(input_id)
		Pswd_list.append(input_pswd)
		print(ID_list)
		print(Pswd_list)
	# elif commit_information == "Delete":
	# 	delete_id = input("Put any id u want to delete")
	# 	delete_pswd = input("Put password to delete for "+delete_id)
		
	# 	del(ID_list[delete_id])
	# 	del(Pswd_list[delete_pswd])

	# 	print(ID_list)
	# 	print(Pswd_list)
	else:
		print("Good bye")
		
		

		


	
		
	
	


# if input_pswd == Pswd_list[0] and input_id == ID_list[0]:
# 	print("Hello "+ID_list[0])
# elif input_pswd == Pswd_list[1] and input_id == ID_list[1]:
# 	print("Hello "+ID_list[1])
# elif input_pswd == Pswd_list[2] and input_id == ID_list[2]:
# 	print("Hello "+ID_list[2])
# else:
# 	print("Sry u put wrong pswd or id")


# if input_pswd == Pswd_list[2] and input_id == ID_list[2]:
# 	print("Hello "+ID_list[2])
# else:
# 	print("Sry u put wrong pswd or id")


	

		
