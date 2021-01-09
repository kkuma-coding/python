w = int(input("Enter a weight: "))     #User enters 1st weight
minimum = w

for i in range(3):
    w = int(input("Enter a weight: "))  #User enters 2nd, 3rd and 4th weight
    if w < minimum:
        minimum = w
