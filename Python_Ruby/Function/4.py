input_id = input("Put your ID\n")

def login_id(_id):
    login_memeber = ['naver', 'google', 'duckduckgo']
    for login_members in login_memeber:
        if login_members == _id:
            return True
    return False   
            
if login_id(input_id):
    print('Hello ' +input_id)
else:
    print('Who are you?')        
