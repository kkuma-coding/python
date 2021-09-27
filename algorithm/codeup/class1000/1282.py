import math
n = int(input())
k = 0

for i in range(1, n):
    if math.sqrt(n-i) % 1 == 0:
        k = i
        n = int(math.sqrt(n-1))
        break

print(k, n)