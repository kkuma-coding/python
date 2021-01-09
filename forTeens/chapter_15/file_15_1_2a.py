x = int(input("Enter an integer (0 - 999): "))

if x <= 9:
    count = 1
elif x <= 99:
    count = 2
else:
    count = 3

print("You entered a ", count, "-digit number", sep = "")
