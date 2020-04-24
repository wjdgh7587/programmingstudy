input_id = input("Type your ID.\n")
input_pswd = input("Push your Password\n")

real_id = "wjdgh7587"
real_pswd = "11"

if real_id == input_id:
	if real_pswd == input_pswd:
		print("Hello "+input_id)
	else:
		print("wrong pswd")
else:
	print("wrong ID")		
				