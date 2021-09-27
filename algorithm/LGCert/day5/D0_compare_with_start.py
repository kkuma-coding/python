"""
<<<입력 설명>>>
첫 줄에 화학물질의 수 N이 입력된다. N의 범위는 1이상 100이하이다.
두 번째 줄부터 N+1줄까지 최저보관온도와 최고보관온도가 입력된다.

보관온도는 -270° ~ 10,000°이며,
각 냉장고는 임의의 정해진 온도를 일정하게 유지할 수 있고,
냉장고는 아주 크다고 가정한다.

<<<출력 설명>>>
첫 줄에 최소로 필요한 냉장고의 대수를 출력한다.

<<<입력 예시>>>
4
-15 5
-10 36
10 73
27 44
<<<출력 예시>>>
2
"""
import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    chems = [list(map(int,readl().split())) for _ in range(N)]
    return N, chems

sol = 0

# 입력받는 부분
N, chems = input_data()
range_list = deque()

# 여기서부터 작성
def solve():
    chems.sort()
    last_e = chems[0][1]
    cnt = 1
    for s, e in chems[1:]:
        if last_e >= s:
            if last_e > e:
                last_e = e
        else:
            cnt += 1
            late_e = e
    return cnt

# 출력하는 부분
print(solve())