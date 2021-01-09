import math
ELEMENTS = 20

values = []
for i in range(ELEMENTS):
    values.append(float(input("Enter a value: ")))

if math.fsum(values) / ELEMENTS < 10:
    print("Average value is less than 10")
