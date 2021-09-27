"""
https://codeup.kr/problem.php?id=4561

첫 째 줄부터 일곱 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100보다 작다.

출력
홀수가 존재하지 않는 경우에는 첫째 줄에 -1을 출력한다.

홀수가 존재하는 경우 첫째 줄에 홀수들의 합을 출력하고, 둘째 줄에 홀수들 중 최소값을 출력한다.

<input>
12
77
38
41
53
92
85

<출력 예시>
256
41
"""
val_list = []
for x in range(7):
    val = int(input())
    if (val % 2 == 1):
        val_list.append(val)

if (len(val_list) == 0):
    print(-1)
else:
    print(sum(val_list))
    print(min(val_list))