"""
문제 [1389] B5: [LAB]숫자 카운팅
실행시간 제한: 1 Sec  메모리사용 제한: 128 MB
제출: 2500  통과: 37.1%

배열에 오름차순으로 N개의 숫자가 저장되어 있다.
M개의 탐색할 숫자가 주어질 때,
각 숫자가 배열에 몇 개씩 저장되어 있는지 출력하는 프로그램을 작성하시오.

<<<입력 설명>>>
첫째 줄에 N 이 입력된다. (1≤N≤200,000)
둘째 줄에 배열에 저장 되어있는 N개의 숫자가 순서대로 공백으로 구분되어 입력된다.
셋째 줄에 M 이 입력된다. (1≤M≤200,000)
넷째 줄에 M개의 탐색할 숫자가 순서대로 공백으로 구분되어 입력된다.
(이 숫자는 정렬 되어있지 않다)
<<<출력 설명>>>
입력 넷째 줄에서 주어진 탐색할 숫자의 배열 내 저장된 개수를 차례대로 출력한다.

<<<입력 예시>>>
10
1 1 1 6 9 11 13 17 19 20
2
1 9
<<<출력 예시>>>
3 1
"""
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    data = [0] + list(map(int, readl().split()))
    M = int(readl())
    num = list(map(int, readl().split()))
    return N, data, M, num


def lower(s, e, d):
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if data[m] == d:
            sol, e = m, m - 1
        elif data[m] > d:
            e = m - 1
        else:
            s = m + 1
    return sol


def upper(s, e, d):
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if data[m] == d:
            sol, s = m, m + 1
        elif data[m] > d:
            e = m - 1
        else:
            s = m + 1
    return sol


# 입력받는 부분
N, data, M, num = Input_Data()

# 여기서부터 작성
l = []
for x in num:
    lo = lower(1, N, x)
    if lo == -1:
        l.append(0)
    else:
        l.append(upper(1, N, x) - lo + 1)

print(*l)