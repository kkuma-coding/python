"""
https://codeup.kr/problem.php?id=2610

10∗10  크기의 그림이 있다.
이 그림에 그림판 색 채우기 기능을 구현하시오.

<<입력 예시>>
__________
_____****_
_____*__*_
__*******_
__*__*_**_
__*__****_
__*____*__
__*____*__
__******__
__________
6 2

<<출력 예시>>
__________
_____****_
_____****_
__*******_
__*__*_**_
__*__****_
__*____*__
__*____*__
__******__
__________
"""

from collections import deque

d = deque()

size = 10
fullmap = []
visit = []

for _ in range(size+2):
    visit.append([False]*(size+2))

fullmap.append([0]*(size+2))
[fullmap.append([0] + [x for x in input()] + [0]) for x in range(size)]
fullmap.append([0]*(size+2))

start_c, start_r = map(int, input().split())

direction = [(-1, 0),(1, 0),(0,-1),(0,1)]

def bfs(sr, sc):
    d.append((sr, sc))

    while d:
        r, c = d.popleft()

        visit[r][c] = True
        if fullmap[r][c] == '*': continue

        fullmap[r][c] = '*'

        for nr, nc in direction:
            rr, cc = nr + r, nc + c
            if visit[rr][cc]: continue
            if fullmap[rr][cc] == 0: continue
            if fullmap[rr][cc] == '_':
                d.append((rr, cc))


bfs(start_r+1, start_c+1)

for i in range(1,size+1):
    for j in range(1,size+1):
        print(fullmap[i][j], end="")
    print()