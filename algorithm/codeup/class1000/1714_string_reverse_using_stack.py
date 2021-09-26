"""
https://codeup.kr/problem.php?id=1714
"""
# 핵심: python의 collections.deque 를 stack 으로 사용한 것.
from collections import deque
d = deque()

val = input()
[d.append(x) for x in val]
while d:
    print(d.pop(), end="")
print()