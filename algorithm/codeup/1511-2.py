# sum of edges
# https://codeup.kr/problem.php?id=1511
size = int(input())

sum = 0
count = 0
for i in range(0, size):
    for j in range(0, size):
        count += 1
        # print (count, end=" ")
        if (i==0 or i==size-1 or j==0 or j==size-1):
            sum += count
    # print()

print (sum)