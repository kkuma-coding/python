def display_menu():
    print("1. Convert USD to Euro (EUR)")
    print("2. Convert Euro (EUR) to USD")
    print("3. Exit")
    print("----------------------------")
    print("Enter a choice: ", end = "")

#Main code starts here 
while True:
    display_menu()
    choice = int(input())

    if choice == 3:
        print("Bye!")
        break
    else:
        amount = float(input("Enter an amount: "))
        if choice == 1:
            print(amount, "USD =", amount * 0.94, "Euro")
        else:
            print(amount, "Euro =", amount / 0.94, "USD")
