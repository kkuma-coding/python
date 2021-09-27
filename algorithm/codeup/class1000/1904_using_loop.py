"""
https://codeup.kr/problem.php?id=1904
"""
a, b = map(int, input().split())

ary_num = [i for i in range(a, b+1)]
ary_bol = [True for _ in range(a, b+1)]

for i in range(len(ary_num)):
    if (ary_bol[i] == False):
        continue
    if (ary_num[i] % 2 == 0):
        ary_bol[i] = False

print (*[ary_num[i] for i in range(len(ary_bol)) if ary_bol[i]])

# print(ary_num)
# print(ary_bol)
# def prime_numbers():