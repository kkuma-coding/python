# factorial 구하기.
# 팩토리알 구하기.

a = int(input())
answer = a
for v in range(a-1, 0, -1):
    answer = answer * v

print(answer)