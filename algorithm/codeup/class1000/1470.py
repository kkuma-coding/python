'''
https://codeup.kr/problem.php?id=1470

입력이 3인 경우 다음과 같이 출력한다.
1 6 7
2 5 8
3 4 9

입력이 5인 경우는 다음과 같이 출력한다.
1 10 11 20 21
2 9 12 19 22
3 8 13 18 23
4 7 14 17 24
5 6 15 16 25
'''

size = int(input())

data = []
for x in range(size):
    data.append([0]*size)

count = 1
for x in range(size): # 가로줄
    for y in range(size): # 세로줄
        data[x][y] = count
        count += 1

for x in range(size):
    for y in range(size):
        if y % 2 == 1:
            print(data[y][size-1-x], end=" ")
        else:
            print(data[y][x], end=" ")
    print()