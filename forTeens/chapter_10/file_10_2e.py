import random        #import random module

#Display a random integer between 10 and 100
print(random.randrange(10, 101))

#Assign a random integer between 0 and 10 to variable y
y = random.randrange(11)
#and display it
print(y)   

#Display a random integer between -20 and 20
print(random.randrange(-20, 21))

#Display a random odd integer between 1 and 99
print(random.randrange(1, 99, 2))

#Display a random even integer between 0 and 100
print(random.randrange(0, 100, 2))
