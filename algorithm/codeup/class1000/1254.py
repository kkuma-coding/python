# https://codeup.kr/problem.php?id=1254
"""
a f
a b c d e f

d g
d e f g
"""
# chr_a = chr('a')
# chr_f = chr('f')

# ord("문자") --> 숫자 값을 얻게 됨
# chr(숫자)   --> 글자 값을 얻게 됨
# print(chr(102))

a, b = input().split()
chr_a = ord(a)
chr_f = ord(b)
for c in range(chr_a, chr_f+1):
    print(chr(c), end=" ")

# print(chr_a, chr_f)
