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
for _ in range(virus_count):
    x, y = map(int, input().split())
    virus.append((x, y))


combi_list = []
for r in range(1, (rect_len//2)+1):
    for c in range(1, (rect_len//2)+1):
        if rect_len == (2 * r) + (2 * c):
            combi_list.append((r, c))

max_count = 0
try_count = 0

for r, c in virus:
    for rlen, clen in combi_list:
        if r + rlen +1 > map_size: continue
        if c + clen +1 > map_size: continue
        for rr in range(r, r + rlen + 1):
            for cc in range(c, c + clen + 1):
                if (rr, cc) in virus:
                    try_count += 1
        # print(f"--virus {r},{c}--> delta {rlen},{clen} : count = {try_count}")
        if try_count > max_count:
            max_count = try_count
        try_count = 0

print(max_count)
