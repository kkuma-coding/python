# https://codeup.kr/problem.php?id=1503

# 하나의 정수N을 입력받아 다음과 같이 작성하시오.
# 지그재그로 출력하시오.
# N이 5라면 다음과 같이 출력한다.
#
# 1  2 3 4 5
# 10 9 8 7 6
# 11 12 13 14 15
# 20 19 18 17 16
# 21 22 23 24 25

# size = 5
size = int(input())
list = list(range(1,(size * size) + 1))
l2 = []
for i in range(0, size):
    if i % 2 == 1:
        l2 = reversed(list[slice(size * i, size * (i+1), 1)])
    else:
        l2 = list[slice(size * i, size * (i+1), 1)]

    for j in l2:
        print(j, end=" ")
    print()