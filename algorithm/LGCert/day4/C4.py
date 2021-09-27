"""
<<<input>>>
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

<<<output>>>
4 3
"""
import sys
from collections import deque

visit = None

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    map_nor_pig = [[0] + list(readl()[:-1])+ [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    map_bg_pig = [[0]*(N+2) for r in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            map_bg_pig[i][j] = map_nor_pig[i][j]
            if map_bg_pig[i][j] == 'R':
                map_bg_pig[i][j] = 'G'
    return N, map_nor_pig, map_bg_pig


sol_nor_pig, sol_rg_pig = -1, -1
# 입력받는 부분


# 여기서부터 작성
# print(N, map_nor_pig)

def flood_fill(r, c, m, value):
    direction = [(0,-1),(0,1),(-1,0),(1,0)]

    q = deque()
    q.append((r,c, value))
    visit[r][c] = True # ****
    cnt = 1

    while (len(q)>0):
        sr, sc, v = q.popleft()
        for dr, dc in direction:
            nr = dr + sr
            nc = dc + sc
            if (visit[nr][nc]==True): continue
            if (m[nr][nc] == v):
                visit[nr][nc] = True
                q.append((nr, nc, v))
                cnt += 1
    return cnt

def solve(m):
    color_count = []
    for r in range(N+1):
        for c in range(N+1):
            if (m[r][c] != 0 and visit[r][c] == False):
                size = flood_fill(r, c, m, m[r][c])
                color_count.append((size, m, m[r][c]))
    return len(color_count)

N, map_nor_pig, map_bg_pig = input_data()
visit = [[False]*(N+2) for _ in range(N+2)]
sol_nor_pig = solve(map_nor_pig)
visit = [[False]*(N+2) for _ in range(N+2)]
sol_rg_pig = solve(map_bg_pig)

# 출력하는 부분
print(sol_nor_pig, sol_rg_pig)
