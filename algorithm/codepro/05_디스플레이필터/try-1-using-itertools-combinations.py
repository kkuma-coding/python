"""
    slts = "0101"
    print(slts.__contains__("0"))
    print(slts.count("0"))

    # branch and bound ??
    # 도로건설 방식?
    # dynamic programming *** 내가 지금 DP 에 약하다.

<input>
4
2 10
2 8
3 4
4 12

<output>
1
"""
from functools import reduce
from itertools import combinations

def func_mul(a, b): return a*b

N = int(input())

R = []
P = []

for i in range(N):
    r, p = map(int, input().split())
    R.append(r)
    P.append(p)


candidate = []
min_diff = 987654321
for x in range(1, N+1):
    combi_list = list(combinations(list(range(N)),x))
    combi_len = len(combi_list)
    for t in combi_list:
        r_mul = 1
        p_sum = 0
        for i in range(x):
            idx = t[i]
            r_mul *= R[idx]
            p_sum += P[idx]
            min_diff = min(min_diff, abs(r_mul-p_sum))
            candidate.append((min_diff, N-x))

candidate.sort(key=lambda x: x[0])
# print(candidate)
print(candidate[0][1])
