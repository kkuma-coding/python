# https://codeup.kr/problem.php?id=1502
# preparation for https://codeup.kr/problem.php?id=1504

# 정수 n이 입력된다. ( 1 <= n <= 100)
# n * n 배열을 수직으로 채워서 출력한다.

# 입력이 2로 주어지면, 아래와 같이 출력한다.
# 1 3
# 2 4

# size = 5
size = int(input())
list = list(range(1,(size * size) + 1))
for i in range(0, size):
    for j in (list[slice (i, size * size, size)]):
        print(j, end=" ")
    print()