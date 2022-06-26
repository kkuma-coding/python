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
            print(data[y][x], end=" ")
        else:
            print(data[y][size-x-1], end=" ")
    print()