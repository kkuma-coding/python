"""
5
1 3 5 6 8
"""
input()
abc_list = input()
abc_list = list(map(int, abc_list.split()))
abc_list.reverse()
print(*abc_list)