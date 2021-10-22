# result = [a*b for a in range(2, 10)
#               for b in range(1, 10)]
# print(result)

# refer to puricare

map_size = 6
combi_list = [(1, 4), (2, 3), (3, 2), (4, 1)]
virus = [(2,2),(4,6),(5,2),(6,4),(2,4),(3,3)]
virus_len = len(virus)

max_count = 0
try_count = 0

# 왠만하면 in 을 쓰지 말자.
# 차라리 len(list(filter, (lambda, list))) 를 쓰자. 훨 빠르다.

for r, c in virus:
    for h, w in combi_list:
        # print(r, c, h, w, list(filter(lambda x: (r <= x[0] <= r+h) and (c <= x[1] <= c+w), virus)))
        try_count = len(list(filter(lambda x: (r <= x[0] <= r + h) and (c <= x[1] <= c+w), virus)))
        # print("----",try_count)
        if max_count < try_count:
            max_count = try_count

print(max_count)

"""
for r, c in virus:
    for h, w in combi_list:
        print(f"r={r},c={c}  delta={h},{w}, to(h,w)={r+h},{c+w}")
        for rr, cc in [(rr, cc) for rr in range(r, r+h+1) for cc in range(c, c+w+1)]:
            print(f"-----{rr},{cc}")
"""