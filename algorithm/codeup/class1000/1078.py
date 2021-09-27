# 2021.3.27 더 이상 python code로 문제를 풀 수 없다.
# c/c++ 로만 접근 가능
num = int(input())
sum = 0

for n in range(1, num+1):
    if (n % 2 == 0):
        sum += n

print(sum)