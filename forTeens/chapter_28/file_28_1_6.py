import random
ELEMENTS = 100

def dice():
    return random.randrange(1, 7)

def search_and_count(x, a):
    count = 0
    for i in range(ELEMENTS):
        if a[i] == x:
            count += 1
    return count

#Main code starts here
a = [None] * ELEMENTS

#Fill the list with random values
for i in range(ELEMENTS):
    a[i] = dice()

x = int(input())
print("Given value exists in the list")
print(search_and_count(x, a), "times")
