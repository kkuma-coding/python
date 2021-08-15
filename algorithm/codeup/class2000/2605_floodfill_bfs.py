"""
[DFS/BFS] 캔디팡 문제
https://codeup.kr/problem.php?id=2605

<input>
2 1 5 1 1 3 4
2 1 5 1 3 5 3
2 3 4 5 2 2 4
4 4 3 2 3 1 3
4 3 5 3 1 4 3
5 4 4 3 3 5 5
2 1 3 5 1 1 2

<output>
4
"""
from collections import deque

size = 7
list_map = []
visit = []

for r in range(size + 2):
    if r == 0 or r == size + 1:
        list_map.append([0] * (size + 2))
    else:
        list_map.append([0] + list(map(int, input().split())) + [0])

for r in range(size + 2):
    visit.append([False] * (size + 2))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

candy_map = {}
rr, cc = 1, 1


def bfs(rr, cc):
    d = deque()
    d.append((rr, cc, list_map[rr][cc]))
    visit[rr][cc] = True

    ret_val = 0

    while d:
        row, col, ap_val = d.popleft()
        visit[row][col] = True
        ret_val += 1

        # print("x,y={},{} val={} #{}".format(row, col, ap_val, ret_val))

        # 주변 block 들 좌표 정보를 queue 에 공급해 준다
        for dr, dc in direction:
            nr, nc = row + dr, col + dc
            if list_map[nr][nc] == 0:
                continue
            if visit[nr][nc]:
                continue
            if ap_val == list_map[nr][nc]:
                d.append((nr, nc, list_map[nr][nc]))

    # print()

    if ret_val >= 3: return True
    return False


answer = 0
for r in range(1, size + 1):
    for c in range(1, size + 1):
        if not visit[r][c]:
            if bfs(r, c):
                answer += 1

print(answer)