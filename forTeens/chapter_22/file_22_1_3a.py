total = 0
count = 0

for i in range(100):
    x = float(input("Enter a number: "))
    if x > 0:
        total += x
        count += 1

if count != 0:
    print(total / count)
else:
    print("No positives entered!")
