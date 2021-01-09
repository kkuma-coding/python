x = int(input("Enter an integer (0 - 999): "))

if x < 0 or x > 999:
    print("Wrong number!")
elif x <= 9:
    print("You entered a 1-digit number")
elif x <= 99:
    print("You entered a 2-digit number")
else:
    print("You entered a 3-digit number")
