# https://codeup.kr/problem.php?id=1508
size = int(input())
map = []
for row in range(0, size):
    map.append(list())
    map[row].append(int(input()))

for ary in map:
    print(ary)