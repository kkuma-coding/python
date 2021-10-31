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


# 왠만하면 in 을 쓰지 말자.
# 차라리 len(list(filter, (lambda, list))) 를 쓰자. 훨 빠르다.

for r, c in virus:
    for h, w in combi_list:
        if r+h > map_size: continue
        if c+w > map_size: continue
        # print(r, c, h, w, list(filter(lambda x: (r <= x[0] <= r+h) and (c <= x[1] <= c+w), virus)))
        for ww in range(w+1): # 이 라인이 가장 magic 같은 라인이다.
            try_count = len(list(filter(lambda x: (r <= x[0] <= r + h)
                                                  and (c-ww <= x[1] <= c+w-ww),
                                        virus)))
            max_count = max(max_count, try_count)

print(max_count)
