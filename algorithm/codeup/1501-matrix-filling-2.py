# https://codeup.kr/problem.php?id=1501
# preparation for https://codeup.kr/problem.php?id=1504

# 정수 n이 입력된다. ( 1 <= n <= 100)
# n * n 배열을 수직으로 채워서 출력한다.

# size = 3
size = int(input())
list = list(range(1,(size * size) + 1))
for i in range(1, size+1):
    for j in (list[slice (size * (i-1), size * i)]):
        print(j, end=" ")
    print()