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
    # print("** accepted: ", wi, "value:", vi)
    if wi > weight:
        continue
    w.append(wi)
    v.append(vi)

count = len(w)-1


d = []
for r in range(count+1):
    d.append(list())
    for c in range(weight+1):
        d[r].append(0)

# for r in range(count+1):
#     print(*d[r])

for i in range(1, count+1):
    # if w[i] > weight:
    #     continue
    # print(f"w[{i}]={w[i]},", end=" ")
    for j in range(0, w[i]):
        d[i][j] = d[i-1][j]
    for j in range(w[i], weight+1):
        # print(f"j={j}, len(d[{i}])={len(d[i])}", weight)
        # print(f"i={i}, j={j}, w[{i}]={w[i]}, d[{i}][{j}]={d[i][j]}")
        d[i][j] = max(d[i-1][j], d[i-1][j-w[i]] + v[i])

# print()

print(d[count][weight])