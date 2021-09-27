"""
덧셈을 못하는 철수를 공부시키기 위해 자연수들을 주고,
그 중에 몇 개의 수를 골라서 그 합이 K가 될 수 있는지 알아보라고 시켰다.
철수 어머니가 자연수들을 무작위로 선택해서 본인도 가능한지 아닌지 모르고 있다.
어머니가 채점을 할 수 있게 주어진 문제의 답을 찾아주자.

첫 번째 줄에 테스트 케이스 개수 T(1≤T≤10)가 주어진다.
두 번째 줄부터 아래 내용이 T개 만큼 주어진다.
첫 줄에 자연수 개수 N(5 <= N <= 20)과 K(1 <= K <= 2,000,000)가 공백으로 구분되어 입력된다.
다음 줄에 N개의 자연수 di(1 <= di <= 100,000)가 공백으로 구분되어 입력된다.

<print>
T줄에 걸쳐 각 테스트 케이스 별로 주어진 자연수 중 몇 개의 합이 K가 되면 “YES”를 아니면 “NO”를 출력한다.

<<<입력 예시>>>
2
5 19
1 2 4 7 10
5 25
1 2 4 7 10
<<<출력 예시>>>
YES
NO
"""
T = int(input())

N = None
K = None
_d = None
arr_pick_or_not = None

def dfs1(n):
    if (n>=N):
        sum = 0
        for i in range(N):
            if(arr_pick_or_not[i] == 1):
               sum += _d[i]
        # print(sum, K)
        return (sum == K)
    for i in range(0, 2):
        arr_pick_or_not[n]=i
        # print(*arr_pick_or_not)
        dfs1(n+1)

for i in range(T) :
    N, K = map(int, input().split())
    _d = list(map(int, input().split()))

    # 여기서부터 작성
    arr_pick_or_not = [0] * N

    if (dfs1(0)):
        print("YES")
    else:
        print("NO")

