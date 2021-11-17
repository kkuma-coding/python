"""
https://codeup.kr/problem.php?id=1535

5
1 3 2 1 3
"""
def getMaxValuePosition(size, int_list):
    if size <= 0:
        return 0
    max_val = sorted(int_list, reverse=True)[0]
    return int_list.index(max_val) + 1

input_size = int(input())
val = list(map(int, input().split()))
solution = getMaxValuePosition(input_size, val)
print(solution)