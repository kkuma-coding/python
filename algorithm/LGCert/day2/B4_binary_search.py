'''
http://www.codexpert.org/problem.php?cid=2104&dv=0&pid=14

첫 번째 줄에 N(1≤N≤50,000)이 주어진다. N은 정렬되어 주어지는 데이터의 수이다.
두 번째 줄에는 N개의 서로 다른 수가 정렬되어 주어진다. 각 수는 공백 하나로 분리되어 주어진다.
세 번째 줄에는 데이터에서 찾아야 할 특정한 수의 개수 T(1≤T≤10,000)가 주어진다. 즉, T가 3이면 3개의 수를 정렬된 데이터에서 찾아야 한다.
네 번째 줄에는 T개의 수가 공백 하나로 분리되어 주어진다.

'''
N = int(input())
data = list(map(int, input().split()))
T = int(input())
num = list(map(int, input().split()))

def bsearch(s, e, d):
    while (s <= e):
        m = (s+e)//2
        if (data[m] == d): return m+1
        elif (data[m] > d): e = m-1
        else: s = m+1
    return 0

l = [bsearch(0, N-1, x) for x in num]
print(*l, sep='\n')