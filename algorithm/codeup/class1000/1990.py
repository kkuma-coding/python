number = input()
sum = 0
for x in number:
    sum += int(x)

if (sum % 3 == 0):
    print(1)
    exit(0)

print(0)