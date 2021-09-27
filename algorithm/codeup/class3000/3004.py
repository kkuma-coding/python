# https://codeup.kr/problem.php?id=3004
'''
5
50 23 54 24 123
'''
count = int(input())
data = input().split()
dec_data_list = [int(d) for d in data]
sorted_dec_data_list = sorted(dec_data_list)

print(sorted_dec_data_list)

for d in dec_data_list:
    print(sorted_dec_data_list.index(d), end=" ")