LAKES = 20

depths = [None] * LAKES
for i in range(LAKES):
    depths[i] = float(input())

#initial value
maximum = depths[0]
#Search furthermore, starting from index 1
for i in range(1, LAKES):
    if depths[i] > maximum:
        maximum = depths[i]

print(maximum)
