"""
input() 읽어들이면서 계산해도 충분하고,
서에서 -> 동쪽 방향으로 (오른쪽으로) 가면서 바로 계산해도 된다는 것.
"""
Q = []

count = int(input())
ans = 0

for _ in range(count):
    h = int(input())
    if not Q:
        Q.append(h)
    else:
        while Q and Q[-1] <= h:
            Q.pop()
        ans += len(Q)
        Q.append(h)

print(ans)