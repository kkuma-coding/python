PEOPLE = 20

first_names = [None] * PEOPLE
last_names = [None] * PEOPLE

for i in range(PEOPLE):
    first_names[i] = input("Enter first name: ")
    last_names[i] = input("Enter last name: ")

needle = input("Enter a first name to search: ")

found = False
for i in range(PEOPLE):
    if first_names[i] == needle:
        print(last_names[i])
        found = True

if found == False:
    print("No one found!")
