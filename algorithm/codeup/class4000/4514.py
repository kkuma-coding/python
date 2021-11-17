"""
https://codeup.kr/problem.php?id=4514

<input>
8 3
5 4 2 6 9 3 8 7

각 그룹의 합 중 최대값이 최소가 되도록 M개의 그룹으로 나누었을 때,
그 최대값을 출력하는 프로그램을 작성하시오.
"""
count, group = map(int, input().split())
marbles = list(map(int, input().split()))

# combination data
combi = []
def combi_gen(ary, remain, depth, group):
    if sum(ary) >= remain:
        return
    if depth >= group:
        return
    for i in range(1, remain+1):
        # if i +
        ary.append(i)
        combi_gen(ary, remain-sum(ary), depth+1, group)

combi_gen(combi, count, 1, group)

print(combi)



d = []
for r in range(len(combi)+1):
    d.append(list())
    for c in range(group+1):
        d.append(0)

# recurrence relation??
