"""
https://codeup.kr/problem.php?id=3740

참조 학습 자료: https://withhamit.tistory.com/332

배낭의 무게 W를 초과하지 않으면서 물건의 가격의 총합의 최대값을 출력한다.

4 5
2 3
1 2
3 3
2 2
"""

count, weight = map(int, input().split())
w = [0]
v = [0]
for _ in range(count):
    wi, vi = map(int, input().split())
    if wi <= weight:
        # print("** accepted: ", wi, "value:", vi)
        w.append(wi)
        v.append(vi)
    else:
        w.append(0)
        v.append(0)


R = max(w) + 1
C = max(v) + 1


d = []
for r in range(R):
    d.append(list())
    for c in range(C):
        d[r].append(0)



for r in range(1, R):
    print(f"{w}, {w[r]}")
    for j in range(0, w[r]):
        d[r][j] = d[r-1][j]
    for j in range(w[r], C):
        d[r][j] = max(d[r-1][j], d[r-1][j-w[r]] + v[r])


for line in d:
    print(*line)


# import sys
# sys.exit(0)


print(d[count][weight])