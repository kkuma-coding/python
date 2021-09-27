"""
문제 [1339] A1: [LAB] 연결된 세포
실행시간 제한: 1 Sec  메모리사용 제한: 128 MB
제출: 1737  통과: 33.8%

당신은 M행, N열의 크기를 가진 행렬을 가지고 있고, 행렬은 1과 0의 세포로 이루어져 있다.
여기서 수직이든 수평이든 대각선 방향이든 인접한 두 개의 세포를 연결되어 있다고 표현하는데,
세포가 1인 것들은 서로 연결되어 하나의 구역을 이룬다.

행렬에는 몇 개의 구역이 있는데, 행렬에서 크기가 가장 큰 구역을 이루는 세포 1의 개수는 얼마인가?

<<<입력 설명>>>
가장 첫 줄에는 행의 크기인 M(0<M<10)을 입력 받고,
두 번째 줄에는 열 크기인 N(0<N<10)을 입력 받는다.
다음으로는 실제 행렬을 입력 받는데, 행렬은 숫자들로 이루어져 있다.

<<<출력 설명>>>
가장 큰 구역의 세포 1의 개수를 출력하라.

<<<입력 예시>>>
4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0

<<<출력 예시>>>
5
"""
import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    M = int(readl())
    N = int(readl())
    map_cell = [[0]*(N+2) if (r==0 or r==M+1) else [0]+list(map(int, readl().split()))+[0] for r in range(M+2)]
    return M, N, map_cell


#입력 받는 부분
M, N, map_cell = Input_Data()
visit = [[False] * (N + 2) for _ in range(M + 2)]

#여기서부터 작성
# print (M, N, map_cell)

size_list = []

def solve():
    count = 0

    q = deque()
    for r in range(1, M+1):
        for c in range(1, N+1):
            if (map_cell[r][c] == 1 and visit[r][c] == False):
                visit[r][c] = True
                count = 1
                q.append((r, c))

                while (len(q)>0):
                    rr, cc = q.popleft()
                    for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0),
                                   (-1,-1), (-1, 1),(1, -1), (1, 1)]:
                        nr = rr + dr
                        nc = cc + dc

                        if visit[nr][nc]: continue
                        if (map_cell[nr][nc] == 1):
                            q.append((nr, nc))
                            count += 1
                            visit[nr][nc] = True
                # end of while()
                size_list.append(count)

    return count

#출력하는 부분
solve()
print(max(size_list))