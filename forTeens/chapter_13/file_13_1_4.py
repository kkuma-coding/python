w1 = int(input("Enter the weight of the 1st person: "))
n1 = input("Enter the name of the 1st person: ")

w2 = int(input("Enter the weight of the 2nd person: "))
n2 = input("Enter the name of the 2nd person: ")

w3 = int(input("Enter the weight of the 3rd person: "))
n3 = input("Enter the name of the 3rd person: ")

maximum = w1
m_name = n1         #This variable holds the name of the heaviest person

if w2 > maximum:
    maximum = w2
    m_name = n2     #Someone else is heavier. Keep his or her name.

if w3 > maximum:
    maximum = w3
    m_name = n3     #Someone else is heavier. Keep his or her name.

print("The heaviest person is", m_name)
print("His or her weight is", maximum)
