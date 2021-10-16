"""
https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/8

<input>
4
2 10
2 8
3 4
4 12

<output>
1
"""
count = int(input())
R = []
P = []
for _ in range(count):
    r, p = map(int, input().split())
    R.append(r)
    P.append(p)


import itertools
combi_list = []
for i in range(1, count+1):
    combi_list += list(itertools.combinations(list(range(count)), i))
# print(type(combi_list[0]))


ans_list = []
for t in combi_list:
    rr = 1
    pp = 0
    for idx in t:
        rr = rr * R[idx]
        pp = pp + P[idx]
    # print("::trying ", t, f'rr={rr}, pp={pp} ',", result=", abs(rr-pp))
    ans_list.append((abs(rr-pp), len(t)))

ans_list.sort(key=lambda x:x[0])
print(count-ans_list[0][1])