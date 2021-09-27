PEOPLE = 100

SSNs = [None] * PEOPLE
first_names = [None] * PEOPLE
last_names = [None] * PEOPLE

for i in range(PEOPLE):
    SSNs[i] = input("Enter SSN: ")
    first_names[i] = input("Enter first name: ")
    last_names[i] = input("Enter last name: ")

needle = input("Enter an SSN to search: ")

found = False
for i in range(PEOPLE):
    if SSNs[i] == needle:
        print(first_names[i], last_names[i])
        found = True
        break

if found == False:
    print("nothing found!")
