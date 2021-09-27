x = int(input("Enter a number: "))

if x < 1 or x > 3:
    print("Invalid Number")
else:
    print("Valid Number")

    if x == 1:          #This is the nested if-elif structure
        print("1st choice selected")
    elif x == 2:
        print("2nd choice selected")
    else:
        print("3rd choice selected")
