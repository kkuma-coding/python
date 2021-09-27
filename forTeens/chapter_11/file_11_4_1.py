import random

last_name = input("Enter last name: ")

#Get a random integer between 100 and 999
random_int = random.randrange(100, 1000)

#Create login ID
login_id = last_name[:4].lower() + str(random_int)

print(login_id)
