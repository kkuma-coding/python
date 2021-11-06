count = int(input())
nums = list(range(1, count+1))

for x in range(count-1):
    nums.remove(int(input()))

print(*nums)