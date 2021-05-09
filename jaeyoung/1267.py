# https://codeup.kr/problem.php?id=1267
"""
5
3 5 7 15 2
"""
n = input()
n = int(n)
numbers = input().split()

sum = 0  # summation = 0

for num in numbers:
    num = int(num)
    if (num % 5 == 0):
        sum = sum + num

print(sum)