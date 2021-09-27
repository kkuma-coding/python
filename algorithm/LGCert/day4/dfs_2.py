N=3
arr = [0]*(N+2)

def dfs2(n, start):
    if (n>N):
        for i in range(1, N+1):
            print(arr[i], end=' ')
        print()
        return
    for i in range(start, 7):
        arr[n]=i
        dfs2(n+1, i)

dfs2(0, 0)