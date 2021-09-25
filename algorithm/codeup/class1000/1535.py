"""
https://codeup.kr/problem.php?id=1535

5
1 3 2 1 3
"""

size = int(input())
val = list(map(int, input().split()))
if size > 0:
    max_val = sorted(val, reverse=True)[0]
    print(val.index(max_val)+1)