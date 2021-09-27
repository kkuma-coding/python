a = [3, 6, 10, 2, 1, 12, 4]
b = sorted(a)

print(a)   #It displays: [3, 6, 10, 2, 1, 12, 4]
print(b)   #It displays: [1  2  3  4  6  10  12]

#sorted() function can be used with tuples as well
c = ("Hermes", "Apollo", "Dionysus")
d = sorted(c, reverse = True)
for element in d:
    print(element, end = "  ")   #It displays: Hermes Dionysus Apollo 

#sorted() function can be used directly in a for statement
for element in sorted(c):
    print(element, end = "  ")   #It displays: Apollo Dionysus Hermes  
