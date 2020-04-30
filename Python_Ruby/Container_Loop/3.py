input_id = input("Puy your id\n")
members = ['naver', 'google', 'daum']
for member in members:
    if member == input_id:
        print('Hello!, '+member)
        import sys #system out
        sys.exit()
print('Who are you?')
