

a = input()
b = input()

len_a, len_b = len(a), len(b)
rev_a, rev_b = a[::-1], b[::-1]

long_len = max(len_a, len_b)
short_len = min(len_a, len_b)
l, s = "", ""
if len_a > len_b:
    l, s = rev_a, rev_b
else:
    l, s = rev_b, rev_a

stack = []
olim = []
sum = 0
remain = 0
for i in range(long_len):
    if i < short_len:
        sum = int(l[i]) + int(s[i])
    else:
        sum = int(l[i])

    if olim:
        sum += olim.pop()

    if sum >= 10:
        olim.append(1)
        remain = sum - 10
    else:
        remain = sum

    stack.append(remain)


if olim:
    stack.append(1)

while stack:
    print(stack.pop(), end="")
print()