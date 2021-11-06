# python 은 memory 를 최적화할 수 있는 언어다???
# 1. 맞다
# 2. 아니다
values = "1 3 5 6 8"
values = list(map(int, values.split()))
# 8 6 4 3 1
print(values)
print(values[::-1]) # python slicing