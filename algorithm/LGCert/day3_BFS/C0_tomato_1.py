'''
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.

철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

<<<입력 설명>>>
첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다.
    M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2≤M, N≤1,000 이다.
    둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
    즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
    하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.

    정수 1은 익은 토마토,
    정수 0은 익지 않은 토마토,
    정수 -1은 토마토가 들어있지 않은 칸

<<<출력 설명>>>
토마토가 모두 익을 때까지의 최소 날짜를 출력.

만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

<<<input>
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

<output>
8
'''
import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int,readl().split())
    map_box = [[0]*(C+2) if (r==0 or r==R+1) else [0]+list(map(int,readl().split()))+[0] for r in range(R+2)]
    return C,R,map_box

sol = -2

# 입력받는 부분
C,R,map_box = Input_Data()
visit = [[False] * (C + 2) for _ in range(R + 2)]

# 작성하는 부분
def solve():
    total_time = 0
    q = deque()

    for r in range(1, R+1):
        for c in range(1, C+1):
            if map_box[r][c] == 1:
                q.append((r, c, 0))
                visit[r][c] = True

    while (len(q)>0):
        sr, sc, time = q.popleft()
        for r, c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr = sr + r
            nc = sc + c
            ntime = time + 1
            total_time = ntime

            if not (1 <= nr <= R): continue
            if not (1 <= nc <= C): continue

            if visit[nr][nc]: continue

            q.append((nr, nc, ntime))
            visit[nr][nc] = True

    return total_time
# 출력하는 부분
sol = solve()
print(sol)