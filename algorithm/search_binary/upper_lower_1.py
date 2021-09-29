"""
10
1 1 1 6 9 11 13 17 19 20
2
1 9
"""
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))


def my_lower(s, e, d):
    sol = -1
    while s <= e:
        m = (s+e) // 2
        if a[m] == d:
            sol = m
            e = m - 1
        elif a[m] < d:
            s = m + 1
        else:
            e = m - 1
    return sol

def my_upper(s, e, d):
    sol = -1
    while s <= e:
        m = (s+e) // 2
        if a[m] == d:
            sol = m
            s = m + 1
        elif a[m] < d:
            s = m + 1
        else:
            e = m - 1
    return sol

low_value = -1
l = []
for x in b:
    low_value = my_lower(0, N-1, x)
    if low_value == -1:
        l.append(0) # not found
    else:
        l.append ( my_upper (0, N-1, x) - low_value + 1)

print(*l)