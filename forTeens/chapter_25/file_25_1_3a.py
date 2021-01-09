DAYS = 31

t = [None] * DAYS

for i in range(DAYS):
    t[i] = int(input())

count = 0
for i in range(DAYS):
    if t[i] < 36:
        count += 1

if count != 0:
    print("There was a possibility of snow in January!")
