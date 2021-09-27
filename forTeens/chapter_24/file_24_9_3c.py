import math
ELEMENTS = 50

values = []
for i in range(ELEMENTS):
    values.append(float(input("Enter a value: ")))

total = math.fsum(values)

print(total)
