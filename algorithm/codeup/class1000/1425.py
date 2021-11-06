"""
https://codeup.kr/problem.php?id=1425

9 6
160 165 164 165 150 165 168 145 170
"""
from collections import deque
count, column = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()

heights = deque(heights)


idx = 1
while heights:
    print(heights.popleft(), end=" ")
    if idx % column == 0:
        print()
    idx += 1