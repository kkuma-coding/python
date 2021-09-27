"""
N명의 점수가 주어질 떄 상위 3명의 ID를 출력하는 프로그램을 작성하시오.

<<<input>>>
8
70 30 70 40 60 50 90 80

<<<output>>>
7 8 1
"""
N = int(input())
arr = list(map(int, input().split()))
arr_idx = [(idx, val) for idx, val in enumerate(arr, 1)]

# print(arr_idx)
arr_idx.sort(key=lambda x:(-x[1], x[0]))
sol = [arr_idx[i][0] for i in range(3)] # tuple 의 0번째 item을 꺼내는 방법.
print(*sol)

# arr_idx.sort(key=lambda: x:(x[1], x[0]))

# print (N, arr)