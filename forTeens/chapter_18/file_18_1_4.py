n = int(input("How many numbers are you going to enter? "))

total = 0

i = 1
while i <= n:
    x = float(input("Enter a number: "))
    total += x
    i += 1

print(total)
