ELEMENTS = 10

b = []
for i in range(ELEMENTS):
    b.append(float(input("Enter a value for element " + str(i) + ": ")))

for i in range(ELEMENTS):
    if b[i] != int(b[i]):
        print("A real found at index:", i)
