"""
<input>
3
041
253
620

<output>
8

본사에서 공장까지 도로를 건설하려고 한다
최소 비용으로 도로를 건설하고자 하는데,
그러기 위해서는 토지 구입 비용을 최소화 해야 한다
지도 정보가 주어졌을 때, 토지를 구입하는 데 드는 최소 비용을 구하시오

[요구사항]

지도 정보
1. 지도는 정사각형 모양으로 크기 N
2. 토지는 1*1 크기로 나줘져 있으며 문자열로 각 토지 구입 가격이 제공됨
3. 구입가격이 0원인 경우는 이미 회사 소유의 토지임을 의미함

토지 구매 시 주의 사항

1. 도로는 상하좌우로 연결되어야 함 (대각선으로 연결은 불가능)
2. 본사는 (0,0) 위치이며, 공장은 N-1, N-1 위치임 (이 땅들은 이미 회사 소유이므로 0원)
3. 구입가격이 0원인 경우는 이미 회사 소유의 토지임을 의미함

토지 구매 시 주의사항

1. 도르는 상하좌우로 연결되어야 함
2. 본사는 (0,0) 위치이며, 공장은 (N-1, N-1) 위치임 (이 땅들은 이미 회사 소유이므로 0원)
   (0,0) 표시는 세로좌표, 가로좌표를 의미함

"""
import sys
from collections import deque
readl = sys.stdin.readline
count = int(readl().strip())

data = []
for i in range(count):
    line = readl().strip()
    list_line = [int(c) for c in line]
    data.append(list_line)


stack = deque()
stack.appendleft((0, 0, 0))

while stack:
    rr, cc, w = stack.pop()

    # r,c combination
    direction = [(0,-1),(0,1),(-1,0),(1,0)]
    for r, c, in direction:
        # print (f"[r:{r}, c:{c}]")
        nr, nc = rr+r, cc+c
        if data[nr][nc] > data[rr][cc] + w:
            data[nr][nc] = data[rr][cc] + w
            stack.appendleft((nr, nc, data[nr][nc]))

print(data[count-1][count-1])