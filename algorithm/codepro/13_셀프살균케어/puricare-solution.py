N, L, M = map(int, input().split())
A = []
for _ in range(M):
    A.append(list(map(int, input().split())))


def calc(r1, r2, c1, c2):
    ret = 0
    for r, c in A:
        if r1 <= r <= r2 and c1 <= c <= c2:
            ret += 1
    return ret


max_count = 0
for r, c in A:
    for h in range(1, L // 2):
        w = L // 2 - h
        for ww in range(w + 1):
            # print(r, r + h, c - ww,  c + w - ww)
            max_count = max(max_count, calc(r, r + h, c - ww, c + w - ww))

print(max_count)