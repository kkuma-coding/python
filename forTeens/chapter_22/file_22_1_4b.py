count_a = 0
count_b = 0

for i in range(10):
    a = int(input("Enter number A: "))
    b = int(input("Enter number B: "))

    if a > b:
        count_a += 1
    elif b > a:
        count_b += 1

print(count_a, count_b)
