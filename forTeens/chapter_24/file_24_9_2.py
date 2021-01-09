ELEMENTS = 100

values = []
for i in range(ELEMENTS):
    values.append(float(input()))

for value in values[::-1]:
    if value > 0:
        print(value)
