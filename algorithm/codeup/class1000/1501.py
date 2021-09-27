# 2 3
# 1 2 3
# 4 5 6

m, n = input().split() # 2, 3
m, n = int(m), int(n) # 2, 3

list = []

for val in range (0, m):
    list.append(input())

for val in list:
    print(val)