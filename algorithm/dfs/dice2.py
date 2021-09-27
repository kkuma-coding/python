# 2021.09.27
_size = 6

def dice(s, d):
    if d <= 0:
        print(*s)
        return
    for x in range(1, _size + 1):
        s.append(x)
        dice(s, d-1)
        s.pop()

stack = []
dice(stack, 3)