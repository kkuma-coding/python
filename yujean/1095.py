# https://codeup.kr/problem.php?id=1095

values = list(map(int, "10 4 2 3 6 6 7 9 8 5".split()))

values.sort()

print(values)
print(values[0])

values.sort(reverse=True)

print(values)
print(values[-1])