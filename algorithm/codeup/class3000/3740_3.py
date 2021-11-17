count, weight = map(int, input().split())

w = [0]
v = [0]
for _ in range(count):
    wi, vi = map(int, input().split())
    if weight < wi: continue
    w.append(wi)
    v.append(vi)

count = len(w) - 1

d = []
for r in range(count+1):
    d.append(list())
    for c in range(weight+1):
        d[r].append(0)

# print(w)
# print(v)

for r in range(1, count+1):
    for c in range(0, w[r]):
        # print("[1]", r, c, d[r][c])
        d[r][c] = d[r-1][c]
    for c in range(w[r], weight+1):
        # print("[2]", r, c, d[r][c])
        d[r][c] = max(d[r-1][c], v[r] + d[r-1][c-w[r]])

print (d[count][weight])