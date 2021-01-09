count1 = 0
count2 = 0
count3 = 0

for i in range(20):
    a = int(input("Enter a number: "))

    if a <= 9:
        count1 += 1
    elif a <= 99:
        count2 += 1
    else:
        count3 += 1

print(count1, count2, count3)
