"""
https://codeup.kr/problem.php?id=1514
"""
from collections import deque

size = 7
spliter_cnt = 3

fmap = []
for _ in range(size):
    fmap.append([0]*size)

spliters = []
for _ in range(spliter_cnt):
    spliters.append(tuple(map(int, input().split())))

for s in spliters:
    rr, cc = s[0]-1, s[1]-1
    fmap[rr][cc] = 2

for s in spliters:
    rr, cc = s[0]-1, s[1]-1
    fmap[rr][cc] = 2

left, right, up, down = (0, -1), (0, 1), (-1, 0), (1, 0)
direction = [left, right, up, down]
d = deque()
def dfs(r, c, dirct):
    d.append((r, c, dirct))

    while d:
        rr, cc, dir = d.popleft()
        if 0 > rr or size <= rr: continue
        if 0 > cc or size <= cc: continue

        if fmap[rr][cc] == 0:
            fmap[rr][cc] = 1
            d.append((rr + dir[0], cc + dir[1], dir))
        elif fmap[rr][cc] == 1:
            # d.append((rr + dir[0], cc + dir[1], dir))
            continue
        elif fmap[rr][cc] == 2:
            fmap[rr][:] = [1 if x == 0 else x for x in fmap[rr]]
            fmap[:][cc] = [1 if x == 0 else x for x in fmap[:][cc]]
            d.append((rr + left[0], cc + left[1], left))
            d.append((rr + right[0], cc + right[1], right))
            d.append((rr + up[0], cc + up[1], up))
            d.append((rr + down[0], cc + down[1], down))

dfs(3, 0, right)

# print answer map
for r in range(size):
    print(*fmap[r])