# https://codeup.kr/problem.php?id=3004
'''
5
50 23 54 24 123
-----------------
2 0 3 1 4

정답을 구할 수는 있지만 codeup.kr의 시간 제한 기준에 걸려 통과되지 않습니다
'''
count = int(input())
data = input().split()

data_num_sort = [int(d) for d in data]
data_num_origin = data_num_sort.copy()

# data_num_sort : 입력 값을 저장한 다음, 정렬할 data
# sort() : 정렬하다
data_num_sort.sort()

for d in data_num_origin:
    print(data_num_sort.index(d), end=" ")

'''
zipped = dict(zip(sorted([int(d) for d in data]), range(len(data))))

sorted_dict = dict(sorted(zipped.items(), key=lambda item: item[0], reverse=False))
for a, b in sorted_dict.items():
    print(a, b)
'''


'''
dec_data_list = [int(d) for d in data]
sorted_dec_data_list = sorted(dec_data_list)

print(sorted_dec_data_list)

for d in dec_data_list:
    print(sorted_dec_data_list.index(d), end=" ")
'''