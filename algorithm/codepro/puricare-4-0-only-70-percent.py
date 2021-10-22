"""
6 10 6
2 2
4 6
5 2
6 4
2 4
3 3


3000 10 6
2 2
4 6
5 2
6 4
2 4
3 3
"""
virus = []

map_size, rect_len, virus_count = map(int, input().split())
vMinX = map_size
vMinY = map_size
vMaxY = 0
vMaxX = 0
for _ in range(virus_count):
    x, y = map(int, input().split())
    virus.append((x, y))
    if vMinX > x: vMinX = x
    if vMinY > y: vMinY = y
    if vMaxX < x: vMaxX = x
    if vMaxY < y: vMaxY = y

# print(f"{vMinX},{vMinY}~{vMaxX},{vMaxY}")


combi_list = []
for r in range(1, (rect_len//2)+1):
    for c in range(1, (rect_len//2)+1):
        if rect_len == (2 * r) + (2 * c):
            combi_list.append((r, c))

max_count = 0
try_count = 0

for r, c in virus:
    for rlen, clen in combi_list:
        if r + rlen > map_size: continue
        if c + clen > map_size: continue
        for rr in range(r, r + rlen):
            for cc in range(c, c + clen):
                # if rr < 0 or rr < vMinX: continue
                # if rr > vMaxX: continue
                # if cc < 0 or cc < vMinY: continue
                # if cc > vMaxY: continue
                if (rr, cc) in virus:
                    try_count += 1
        # print(f"--virus {r},{c}--> delta {rlen},{clen} : count = {try_count}")
        if try_count > max_count:
            max_count = try_count
        try_count = 0

print(max_count)
