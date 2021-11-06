# https://codeup.kr/problem.php?id=1093
# 1093번이 python 으로는 제출이 되지 않는다.
total = 23
count = int(input())
calls = list(map(int, input().split()))

class1 = dict.fromkeys(range(1, total+1), 0)
for n in calls:
    class1[n] += 1
print(*class1.values())