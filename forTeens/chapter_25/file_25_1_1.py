ELEMENTS = 20

#Read lists a and b
a = [None] * ELEMENTS
b = [None] * ELEMENTS
for i in range(ELEMENTS):
    a[i] = float(input())
for i in range(ELEMENTS):
    b[i] = float(input())

#Create list new_arr
new_arr = [None] * ELEMENTS
for i in range(ELEMENTS):
    if a[i] > b[i]:
        new_arr[i] = a[i]
    else:
        new_arr[i] = b[i]

#Display list new_arr
for element in new_arr:
    print(element)
