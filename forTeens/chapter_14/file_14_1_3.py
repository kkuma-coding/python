COEFFICIENT = 3.785

print("1: Gallons to liters")
print("2: Liters to gallons")
choice = int(input("Enter choice: "))

quantity = float(input("Enter quantity: "))

if choice == 1:
    result = quantity * COEFFICIENT
    print(quantity, "gallons =", result, "liters")
else:
    result = quantity / COEFFICIENT
    print(quantity, "liters =", result, "gallons")
