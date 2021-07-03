# https://codeup.kr/problem.php?id=6040
# [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기(설명)(py)


# 10 / 3 --> 3 (나머지 1)
# 11 / 3 --> 3 (나머지 2)

# 10 3
a, b = input().split()
a, b = int(a), int(b)

print(a // b)
