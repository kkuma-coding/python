a = float(input("Enter 1st number: "))
op = input("Enter type of operation: ")    #Variable op is of type string
b = float(input("Enter 2nd number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Error: Division by zero")
    else:
        print(a / b)
