# https://codeup.kr/problem.php?id=1367
n = int(input())
for i in range(n):
    padding = " " * (n - i-1)
    print(padding, end="")
    for j in range(n):
        print("*", end="")
    print()