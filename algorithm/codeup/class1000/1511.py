# sum of edges
# https://codeup.kr/problem.php?id=1511
size = int(input())

count = 0
for i in range(0, size):
    for j in range(0, size):
        count += 1
        print (count, end=" ")
    print()