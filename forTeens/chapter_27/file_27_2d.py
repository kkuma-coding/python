#Define the function 
def get_fullname():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    return first_name, last_name

#Main code starts here
fname, lname = get_fullname()
print("First name:", fname)
print("Last name:", lname)
