memo = {}
count, ask = map(int, input().split())
for _ in range(count):
    name, cnt = input().split()
    cnt = int(cnt)
    # print("input value:::", name, cnt)
    if name in memo:
        memo[name] += int(cnt)
    else:
        memo[name] = int(cnt)
    # print(memo)

for _ in range(ask):
    name = input()
    if name in memo:
        print(memo[name])
    else:
        print(0)
