n = int(input("How many numbers are you going to enter? "))

total = 0
for i in range(n):
    x = float(input("Enter number No" + str(i + 1) + ": "))
    total = total + x

if n > 0:
    average = total / n
    print("The average value is:", average)
else:
    print("You didn't enter any number!")
