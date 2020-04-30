puts("Put your id")
input_id = gets.chomp()
members = ['naver', 'google', 'daum']
for member in members do
    if member == input_id
        puts('Hello!, '+member)
        exit #system out
    end
end     
puts('Who are you?')
