import sys

INF = 987654321

readl = sys.stdin.readline
count = int(readl().strip())

data = []
dist = []

for _ in range(count):
    l = readl().strip()
    data.append([int(c) for c in l])
    dist.append([INF]*count)


direction = [(-1, 0),(1, 0),(0, -1),(0, 1)]
stack = [] # most simple stack usage at this time

dist[0][0] = 0

stack.append((0,0,0)) # r, c, w_dist
while stack:
    r, c, w_dist = stack.pop()

    if w_dist > dist[r][c]: continue
    if r == count - 1 and c == count -1: continue

    for rr, cc in direction:
        nr, nc = rr+r, cc+c
        if not (0 <= nr < count and 0 <= nc < count): continue
        if dist[nr][nc] > w_dist + data[nr][nc]:
            dist[nr][nc] = w_dist + data[nr][nc]
            # data[nr][nc] 를 넣어주는게 아니라 dist[nr][nc] 를 넣어주어야 한다
            # 왜냐하면, dist matrix 에 update 하면서 얻어내는 가중치를 기반으로
            # 최종 종착지까지의 link 를 만들어 내야 하기 때문이다.
            # stack.append((nr, nc, dist[nr][nc]))
            stack.insert(0, (nr, nc, dist[nr][nc]))

print(dist[count-1][count-1])