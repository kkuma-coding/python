N=3
arr = [0]*(N+2)
flag = [0]*(N+2)

"""
def Dice3(n):
    if n >= N:
        print(*num[:N])
        return
    for i in range(1, 7):
        if flag[i]: continue
        num[n] = i
        flag[i] = 1
        Dice3(n + 1)
        flag[i] = 0
"""
def dfs3(n):
    if (n>N):
        print(*arr[:N])
        return
    for i in range(1, 7):
        if flag[i]: continue
        arr[n]=i
        flag[i] = 1
        dfs3(n+1)
        flag[i] = 0

dfs3(0)