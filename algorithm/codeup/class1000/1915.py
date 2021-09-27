"""
https://codeup.kr/problem.php?id=1915
"""
memo = {1:1, 2:1}
def fib(n):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# print(fib(1))
# print(fib(2))
print(fib(int(input())))