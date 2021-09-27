"""
<<<input>>>
5
1 3
2 5
8 10
4 7
6 9

<<<output>>>
3
"""
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int,readl().split())) for _ in range(N)]
    return N, info

sol = -1

#입력받는 부분
N, info = Input_Data()

#여기서부터 작성
# 영화를 아무리 오래 봐도 6개로 (1~12)시로 제한
#
time_start_end = dict()
for i in range(1, 12):
    time_start_end[i] = time_start_end.setdefault(i, [])

for a, b in info:
    time_start_end[a] = time_start_end.setdefault(a, []) + [b]

for a in time_start_end:
    time_start_end.get(a).sort()

count = 0
for a in time_start_end:
    time_start_end.get(a)
    count += 1

# 출력하는 부분
print(count)
