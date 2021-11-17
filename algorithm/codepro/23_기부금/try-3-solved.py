"""
5 20
4 42 40 26 46
"""
import sys

readl = sys.stdin.readline

emply_cnt, M = map(int, readl().strip().split())
A = []

max_A = 0
str_data = readl().strip()
for v in str_data.split():
    int_v = int(v)
    if max_A < int_v: max_A = int_v
    A.append(int_v)


def check(mid):
    global A, M, emply_cnt
    sum = M
    for i in range(emply_cnt):
        if A[i] <= mid: continue
        sum -= A[i] - mid
        # print(f"--- sum={sum}, A[i]={A[i]}, mid={mid}")
        if sum <= 0: return True

    return False


s, e = 0, max_A
m = 0
solution = 0

# 컨셉이 다르다.
while s <= e:
    m = (s+e) // 2
    if check(m):
        s = m + 1
        solution = m
        # print(f"s={s}, e={e}, m={m}, solution={solution}")
    else:
        e = m - 1

print(solution)