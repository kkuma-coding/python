a = [3, 60, 15]
print(a[1])                   #It displays: 60
del a[1]
print(a)                      #It displays: [3, 15]
print(a[1])                   #It displays: 15

b = [5, 2, 10, 12, 23, 6]
del b[2:5]
print(b)                      #It displays: [5, 2, 6]

#Clear the list
del b[:]
print(b)                      #It displays: []
