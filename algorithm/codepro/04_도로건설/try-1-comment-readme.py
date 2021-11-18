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
INF = 987654321
data = []
value_map = []
for i in range(count):
    line = readl().strip()
    list_line = [int(c) for c in line]
    data.append(list_line)
    value_map.append([INF]*count)

# value_map = data.copy()
value_map[0][0] = 0

"""
###### debugging purpose
for i in range(count):
    print(*data[i])
print("-------------------------------")
for i in range(count):
    print(*value_map[i])
print("-------------------------------")
"""


stack = deque()
stack.appendleft((0, 0, 0))

while stack:
    rr, cc, w = stack.pop()

    # 나는 문제 정의에 따라 "최소값"을 찾아가고 있다.
    # map 은 value_map, data 두 개이고, 계산 결과 반영은 value_map
    # 기껏 value_map 에 낮은 candidate 을 비용들여서 얻어둬 놓고,
    # 즉, 애써 얻어둔 value_map[rr][cc] 를 w로 덮어쓰지 말라는 것.
    # 그럼 똑같은 계산을 다시 해야 하는 일이 발생한다.
    # w는 data[rr][cc] 값이 stack 을 거쳐서 치환되어 전달된 값이다.
    if value_map[rr][cc] > w: continue

    # rr, cc 는 근거지 position 이다.
    # while 내에서 stack 에 추가된 걸 꺼내가면서 candidate 을 하나씩 검토하는 식인데,
    # 최종 답안을 구해야 할 point에서 발현되는 stack.append() 로 인한 계산은 할 필요 없다.
    # 최종 종착지 답안지에서 퍼져나가는 stack 추가 propagation 은 최종 답안을 망가뜨리는 일 뿐이다.
    if rr == count -1 and cc == count -1: continue

    # r,c combination
    direction = [(0,-1),(0,1),(-1,0),(1,0)]
    for r, c, in direction:
        nr, nc = rr+r, cc+c
        if 0 <= nr < count and 0 <= nc < count:
            if value_map[nr][nc] > data[rr][cc] + w:
                # print (f"[{rr}:{cc}] -> [{nr}:{nc}] {value_map[nr][nc]}")
                value_map[nr][nc] = data[rr][cc] + w
                stack.appendleft((nr, nc, value_map[nr][nc]))

"""
for i in range(count):
    print(*value_map[i])
"""

print(value_map[count-1][count-1])