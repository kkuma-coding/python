# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
'''
도로: '.'
공원: 'X'

출발위치 (0,0)
도착위치 (H-1, W-1)

필요한 최소 시간은?
-----------------------------
<<input>>
3 3
...
...
...
<<output>>
4
-----------------------------
<<input>>
5 4
..X.
X...
..XX
.X..
....
<<output>>
9
-----------------------------
<<input>>
8 10
..........
XXXXX.....
....X.....
....X.....
....XXXX..
.......X..
.......XXX
..........

<<output>>
-1
-----------------------------
        상,  하,  좌,   우
column ( 0) (0) (-1)  (1)
row    (-1) (1) ( 0)  (0)
'''
import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_park = [['X']+list(readl()[:-1])+['X'] if 1<=r<=R else ['X']*(C+2) for r in range(R+2)]
    return R, C, map_park

# 입력받는 부분
R, C, map_park = input_data()

# 여기서부터 입력
sol = -1
visit = None

def BFS():
    q = deque()
    visit = [[0] * (C + 2) for _ in range(R + 2)]

    visit[1][1] = 1
    q.append((1,1,0))

    while len(q)>0:
        r, c, time = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc, ntime = dr + r, dc + c, time+1

            # 범위 밖: 걸러내기
            if not (1<=nc<=C): continue
            if not (1<=nr<=R): continue
            if (map_park[nr][nc] == 'X'): continue
            if (visit[nr][nc] == 1): continue

            if (nr == R and nc == C): return ntime
            # print(map_park[nr][nc], ntime)

            q.append((nr, nc, ntime))
            visit[nr][nc] = 1

    return -1

# 출력하는 부분
sol = BFS()
print(sol)