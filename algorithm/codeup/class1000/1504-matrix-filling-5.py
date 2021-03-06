# https://codeup.kr/problem.php?id=1504

# 하나의 정수 N을 입력받아 다음과 같이 지그재그로 출력하시오.
# N이 3이라면,
#
# 1 6 7
# 2 5 8
# 3 4 9

# size = 5
size = int(input())

my_list = []
gen = list(range(1,(size * size) + 1))

for i in range (0, size):
    if i % 2 == 1:
        my_list.append(list(reversed(gen[slice(size * i, size * (i+1), 1)])))
    else:
        my_list.append(gen[slice(size * i, size * (i+1), 1)])

for i in range(0, size):
    for j in range(0, size):
        print (my_list[j][i], end=" ")
    print()