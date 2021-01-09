w1 = int(input("Enter the weight of the 1st person: "))
w2 = int(input("Enter the weight of the 2nd person: "))
w3 = int(input("Enter the weight of the 3rd person: "))
w4 = int(input("Enter the weight of the 4th person: "))

#memorize the weight of the first person
minimum = w1

#If second one is lighter, forget
#everything and memorize this weight
if w2 < minimum:
    minimum = w2

#If third one is lighter, forget
#everything and memorize this weight
if w3 < minimum:
    minimum = w3

#If fourth one is lighter, forget
#everything and memorize this weight
if w4 < minimum:
    minimum = w4

print(minimum)
