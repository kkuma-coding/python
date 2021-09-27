ELEMENTS = 20

values = []
for i in range(ELEMENTS):
    values.append(float(input("Enter a value: ")))

#Accumulate values in total
total = 0
for i in range(ELEMENTS):
    total = total + values[i]

average = total / ELEMENTS

if average < 10:
    print("Average value is less than 10")
