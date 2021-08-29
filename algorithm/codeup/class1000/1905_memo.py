"""
https://codeup.kr/problem.php?id=1905
"""

"""
import sys
sys.setrecursionlimit(5000)

memo = {1: 1,
        2: 3,
        3: 6,
        10: 55, 100:5050}

def add(n):
    if n in memo:
        return memo[n]
    memo[n] = n + add(n-1)
    return memo[n]
"""

input_val = int(input())
middle = input_val // 2
remain = input_val % 2

sum = (1 + input_val) * middle
if (remain > 0):
    sum += (middle + remain)

print (sum)