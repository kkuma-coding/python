from collections import deque
d = deque()

count = int(input())
values = input()
[d.append(x) for x in list(map(int, values.split()))]

for _ in range(count):
    for num in d:
        print(num, end=" ")
    print()
    x = d.popleft()
    d.append(x)