# https://codeup.kr/problem.php?id=1083
num = int(input())

for n in range(1, num+1):
    if (n % 3 ==0):
        print("X", end=" ")
    else:
        print (n, end=" ")

for n in range(1, num+1):
    print('X' if n % 3 == 0 else n, end=" ")
