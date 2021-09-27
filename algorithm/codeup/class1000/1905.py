"""
https://codeup.kr/problem.php?id=1905
"""
import sys
sys.setrecursionlimit(5000)

memo = {1:1,            10:5050,
        500:130245,     1000:505495,
        2000:2005995,   3000:4506495,
        4000:8006995,   5000:12507495,
        6000:18007995,  7000:24508495,
        8000:32008995,  9000:40509495,
        10000:50009995, 11000:60510495
        }

def addition(n):
    if (n in memo):
        return memo[n]
    memo[n] = n + addition(n-1)
    return memo[n]

print(addition(int(input())))