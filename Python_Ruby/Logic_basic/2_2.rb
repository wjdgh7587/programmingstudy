puts("type your ID")
input_id = gets.chomp()

puts("type your PASSWORD")
input_pswd = gets.chomp()

real_id = "wjdgh7587"
real_pswd = "11"

if real_id == input_id and real_pswd == input_pswd
        puts("Hello "+input_id)
else
    puts("wrong ID")  
end	