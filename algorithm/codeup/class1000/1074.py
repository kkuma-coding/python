# https://codeup.kr/problem.php?id=1074
# [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)
count = int(input())

for n in range(count, 0, -1):
    print(n)

"""
while (count >= 1):
    print(count)
    count = count - 1
"""