"""
https://codeup.kr/problem.php?id=1904
"""
import math

a, b = map(int, "2 7".split())

ary_num = [i for i in range(a, b+1)]
ary_bol = [True for _ in range(a, b+1)]

for i in range(len(ary_num)):
    if (ary_bol[i] == False):
        continue
    dividor = int(math.sqrt(ary_num[i]))
    if (dividor == 1):
        continue
    if (ary_num[i] % dividor == 0):
        ary_bol[i] = False

print ([ary_num[i] for i in range(len(ary_bol)) if ary_bol[i]])

# print(ary_num)
# print(ary_bol)
# def prime_numbers():