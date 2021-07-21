"""
첫째 줄에 입체기동장치의 갯수 n이 입력된다. (1 <= n <= 100)

둘째 줄부터 n+1째 줄까지 각 줄에 입체기동장치의 식별번호 a와 가스 보유량 b가 주어진다.

a는 중복 될 수 없지만 b는 중복될 수 있다. (1 <= a <= 100), (0 <= b <= 10,000)

<<<출력>>>
첫째 줄부터 n번째 줄까지 각 줄에 식별번호를 오름차순으로 정렬해 가스 보유량과 같이 출력한다.

<<<입력 예시>>>
3
2 10
3 20
1 30

<<<출력 예시>>>
1 30
2 10
3 20
"""
import sys
readl = sys.stdin.readline
N = int(readl())
input_values = []
for _ in range(N):
    a, b = map(int, readl().split())
    input_values.append((a, b))

input_values.sort(key=lambda x: (x[0]))
for a, b in input_values:
    print(a, b)