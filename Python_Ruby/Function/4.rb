puts("Put your ID")
input_id = gets.chomp()
 
def login(_id)
  members = ['naver', 'google', 'duckduckgo']
  for member in members do
      if member == _id
          return true
      end
  end
  return false
end
 
if login(input_id)
  puts('Hello, '+input_id)
else
  puts('Who are you?')
end