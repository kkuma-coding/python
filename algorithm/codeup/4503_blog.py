from collections import deque

n = int(input())
pair = int(input())
info = dict()

for i in range(pair):
    com1, com2 = map(int, input().split())

    info[com1] = [com2]
    info[com2] = [com1]
    # info[com1] = info.setdefault(com1, []) + [com2]
    # info[com2] = info.setdefault(com2, []) + [com1]

print(info)