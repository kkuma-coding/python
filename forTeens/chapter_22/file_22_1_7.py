answer = "yes"       #Initialization of answer

while answer.upper() == "YES":
    a = int(input("Enter number A: "))
    b = int(input("Enter number B: "))

    result = a ** b
    print("The result is:", result)

    answer = input("Would you like to repeat? ")
