ELEMENTS = 8

values = []
for i in range(ELEMENTS):
    values.append(float(input("Enter a value for element " + str(i) + ": ")))

#Display the elements with odd-numbered indexes
for value in values[1:ELEMENTS:2]:         #Start from 1 and increment by 2
    print(value)
