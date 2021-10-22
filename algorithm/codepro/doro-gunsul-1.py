"""
https://codepro.lge.com/exam/18/국내-연습문제/quiz/7

본사에서 공장까지 도로를 건설하려고 한다
최소 비용으로 도로를 건설하고자 하는데,
그러기 위해서는 토지 구입 비용을 최소화 해야 한다
지도 정보가 주어졌을 때, 토지를 구입하는데 드는 최소 비용을 구하시오

<input>
3
041
253
620

<output>
8
"""
from collections import deque

WALL = -1
maps = []
visit = []
count = int(input())
maps.append([-1]*(count+2))
for _ in range(count):
    maps.append([WALL] + [int(c) for c in input()] + [WALL])
maps.append([WALL]*(count+2))


for _ in range(count+2):
    visit.append([0]*(count+2))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

paths = []

stack = deque()

def dfs(r, c, along):
    if maps[r][c] == WALL: return
    if visit[r][c]: return

    stack.append((r, c))
    visit[r][c] = 1

    while stack:
        rr, cc = stack.pop()
        for dr, dc in direction:
            dfs(dr+rr, dc+cc)


dfs(1, 1)
print(paths)