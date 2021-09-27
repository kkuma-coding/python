LAKES = 20

names = [None] * LAKES
depths = [None] * LAKES
countries = [None] * LAKES
areas = [None] * LAKES

for i in range(LAKES):
    names[i] = input()
    depths[i] = float(input())
    countries[i] = input()
    areas[i] = float(input())

#Find the maximum depth and
#the index in which this maximum depth exists
maximum = depths[0]
index_of_max = 0
for i in range(1, LAKES):
    if depths[i] > maximum:
        maximum = depths[i]
        index_of_max = i

#Display information using index_of_max as index
print(depths[index_of_max], names[index_of_max])
print(countries[index_of_max], areas[index_of_max])
