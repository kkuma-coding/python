"""
https://codeup.kr/problem.php?id=3170

<<input>>
3 4
ddobot 3
poketmon 5
ddobot 7
ddobot
poketmon
ddobot
hellocarbot

<<outout>>
10
5
10
0
"""

memo = {}
count, ask = map(int, input().split())
for _ in range(count):
    name, cnt = input().split()
    memo[name] = memo.get(name, 0) + int(cnt)

query = [input() for _ in range(ask)]

answer = [memo.get(q, 0) for q in query]

for a in answer:
    print(a)