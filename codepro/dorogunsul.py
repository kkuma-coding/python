"""
3
041
253
620
"""
count = int(input())
lines = []
for _ in range(count):
    line = input()
    lines.append([int(c) for c in line])

d = []
d.append([0]*(count+1))
for l in lines:
    d.append([0]+l)

# for l in d:
#     print(*l)

for r in range(1, 10):
    for c in range(count+1):
        d[r][c] = d[r-1][c]