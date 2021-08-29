"""
https://codeup.kr/problem.php?id=1714
"""
from collections import deque
d = deque()

val = input()
[d.append(x) for x in val]
while d:
    print(d.pop(), end="")
print()