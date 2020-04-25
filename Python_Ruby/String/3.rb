#!/usr/bin/ruby
puts("egoing's \"tutorial\"")
#escape 역슬래시는 아주 특별한 문자를 가지고 있는 문자이다.
puts("\\") #=puts("Hello)
#따옴표가 나오면 컴퓨터는 문자가 오는구나라고 생각하고 그 뒤에 \가 오면 역으로 특수문자가 오는구나 하면서 오류가 발생한다.
#즉 문자가 닫히지 않는것으로 인식한다.
puts("Hello\nworld") #\n은 줄 바꾸기 n은 New Line의 약자이다.
puts("Hello\t\tworld")#\t는 들여쓰기이다.
puts("\a") #알람
puts('Hello\nworld') #루비에서는 작은따옴표와 큰따옴표가 미묘하게 다르지만 파이썬에서는 똑같다.

puts(10+5)
puts("10"+"5")
