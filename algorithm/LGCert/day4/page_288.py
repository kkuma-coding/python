"""
<<<input>>>
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

<<<output>>>
3
7
8
9
--------------------------------------

<<<input>>>
7
0110011
0011000
1010000
1011110
1000011
0111101
0100101

<<<output>>>
4
2
3
6
13
"""

import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    # map_apt = [[0]*(N+2) if (n==0 or n==N+1) else [0]+list(map(int,readl().split()))+[0] for n in range(N+2)]
    map_apt = [[0] + list(map(int,list(readl().strip()))) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N,map_apt

N, map_apt = Input_Data()
# print(N, map_box)

def flood_fill(r, c):
    direction = [(0,-1),(0,1),(-1,0),(1,0)]
    q = deque()
    q.append((r,c))
    map_apt[r][c] = 0  # *****

    cnt = 1
    while (len(q)>0):
        sr, sc = q.popleft()
        for dr, dc in direction:
            nr = dr + sr
            nc = dc + sc
            if (map_apt[nr][nc]==0):
                continue
            map_apt[nr][nc] = 0
            q.append((nr, nc))
            cnt += 1
    return cnt

def solve():
    list_size = []
    for r in range(N+1):
        for c in range(N+1):
            if (map_apt[r][c] == 1):
                size = flood_fill(r, c)
                list_size.append(size)
    list_size.sort()
    return len(list_size), list_size

size, list_size = solve()
print(size)
print(*list_size, sep='\n')