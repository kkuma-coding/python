import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    map_cost = [[0] + list(map(int, readl()[:-1])) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_cost

sol = -2
# 입력받는 부분
N, map_cost = input_data()

# 여기서부터 작성
def solve():
    MAX = 9999
    visit = [[MAX]*(N+2)]
    q = deque()

    q.append((1,1,0))

    while len(q)>0:
        pass

    return 0

# 출력하는 부분
print(solve())
"""
3
041
253
620
------
8
"""