# https://codeup.kr/problem.php?id=1286

data_list = []
for i in range(5):
    data_list.append(int(input()))

data_list.sort()

print(data_list.pop())
print(data_list[0])