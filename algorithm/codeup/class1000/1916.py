memo = {1:1,
        2:1}

def fib(n):
    if (n in memo):
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(int(input())) % 10009)