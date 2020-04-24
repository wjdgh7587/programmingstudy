puts("type your ID\n")
input_id = gets.chomp()

puts("type your PASSWORD\n")
input_pswd = gets.chomp()

real_id = "wjdgh7587"
real_pswd = "11"

if real_id == input_id
    if real_pswd == input_pswd
        puts("Hello "+input_id)
        puts("wrong paswd")
    else
        puts("wrong password")
    end
else
    puts("wrong ID")  
end	