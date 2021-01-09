LAKES = 20

names = [None] * LAKES
depths = [None] * LAKES

#Read names and depths
for i in range(LAKES):
    names[i] = input()
    depths[i] = float(input())

#Find maximum depth
maximum = depths[0]
m_name = names[0]
for i in range(1, LAKES):
    if depths[i] > maximum:
        maximum = depths[i]
        m_name = names[i]

print(m_name)
