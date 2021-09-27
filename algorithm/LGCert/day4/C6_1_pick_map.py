N=5
arr = [0]*(N+2)

def dfs1(n):
    if (n>N):
        for i in range(1, N+1):
            print(arr[i], end=' ')
        print()
        return
    for i in range(0, 2):
        arr[n]=i
        dfs1(n+1)

dfs1(0)