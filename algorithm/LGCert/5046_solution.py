import sys
"""
Problem: 5046
User: SWT01006
Language: Python
Result: Accepted
Time: 1836 ms
Memory: 44648 kb
"""

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    intvals = [list(map(int, readl().split())) for _ in range(M)]
    return N, M, intvals


def check(d):
    idx = 0
    last = intvals[0][0]

    for _ in range(N - 1):
        while idx < M and intvals[idx][1] < last + d:
            idx += 1
        if idx == M: return False
        last = intvals[idx][0] if intvals[idx][0] > last + d else last + d
    return True


def Get_Solution():
    intvals.sort()
    s, e = 0, intvals[-1][1]

    while s <= e:
        m = (s + e) // 2
        if check(m):
            sol = m
            s = m + 1
        else:
            e = m - 1
    return sol


sol = -1
# 입력받는 부분
N, M, intvals = Input_Data()

# 여기서부터 작성
sol = Get_Solution()

# 출력하는 부분
print(sol)
