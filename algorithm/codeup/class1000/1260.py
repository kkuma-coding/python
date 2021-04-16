# https://codeup.kr/problem.php?id=1260
sum = 0
input_list = input().split()
a, b = [int(a) for a in input_list]
for value in range(a, b+1):
    if (value % 3 == 0):
        sum += value

print(sum)