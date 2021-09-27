# 2021.09.25

loop_cnt = 6
message = list()


def dice(q, depth):
    if depth <= 0:
        print(*q)
        q.pop()
        return
    for i in range(1, loop_cnt + 1):
        q.append(i)
        dice(q, depth - 1)
    if q:
        q.pop()


dice(message, 3)
