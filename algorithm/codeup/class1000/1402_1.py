cnt = int(input())
num_list = input()

num_list = list(map(int, num_list.split()))
num_list.reverse()
print(*num_list)