print(type('first_container')) #<class 'str'>
name = 'first_container'
print(name+"\n") #'first container'

print(type(['first_container', 'second_container', 'third_container'])) 
#<class 'list'>
names = ['first_container', 'second_container', 'third_container']
print(names)
print("")

print(names[0]) #first container
print(names[1]) #second container
print(names[2]+"\n") #third container
print(names[0]+" the next container is "+names[1]+"\n")

first_container = ['programmer', 'Jeonju', 28, False]
print(first_container)
first_container[1] = 'Seoul' # put 'Seoul' instead of 'Jeonju'
print(first_container)

# print(first_container) #['programmer', Seoul', 28, False]