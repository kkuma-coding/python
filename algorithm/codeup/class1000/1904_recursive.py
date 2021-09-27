"""
https://codeup.kr/problem.php?id=1904
"""

odds_list = []

a, b = map(int, input().split())
# a, b = map(int, "2 7".split())

def odd(n):
    if (n > b):
        return
    if (n % 2 == 1):
        odds_list.append(n)
    odd(n+1)

odd(a)
print(*odds_list)
# print(ary_num)
# print(ary_bol)
# def prime_numbers():