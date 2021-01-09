DAYS = 31

t = [None] * DAYS

for i in range(DAYS):
    t[i] = int(input())

found = False
for i in range(DAYS):
    if t[i] < 36:
        found = True

if found == True:
    print("There was a possibility of snow in January!")
