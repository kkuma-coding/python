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
    if x % 2 == 0:
        print(*data[x][::-1]) # slice
    else:
        print(*data[x])