# http://www.codexpert.org/problem.php?cid=2104&dv=0&pid=10
'''
문제 [2679] B0: [LAB] 프린터 큐
실행시간 제한: 1 Sec  메모리사용 제한: 128 MB
제출: 2594  통과: 38.4%

컴퓨터 과학과 학생회의 유일한 프린터는 매우 무거운 작업량을 겪고 있다.
때로는 수백 개의 작업으로 인해 한 페이지 출력을 얻으려면 몇 시간을 기다려야 할 수 있다.
일부 작업이 다른 작업보다 중요하기 때문에 학생회의 회장인 철수는
대기 열에 대한 간단한 우선 순위 시스템을 발명하고 구현했다.
이제 각 작업에 우선 순위가 1과 9 사이(9가 가장 높은 우선 순위이고 1이 가장 낮음)에서 지정된다.

프린터는 다음과 같이 작동한다.

- 대기 열의 첫 번째 작업인 J를 대기 열에서 가져옴.
- 대기 열에 작업 J보다 우선 순위가 높은 작업이 있는 경우, J를 인쇄하지 않고 대기 열 끝으로 이동 시킴.
- 그렇지 않으면 작업 J를 인쇄 함 (다시 대기 열에 넣지 않음)

이러한 방식의 발명으로 우선순위가 높은 중요한 문서는 매우 빨리 인쇄되지만,
중요도가 낮은 다른 문서들은 인쇄되기까지 꽤 오래 기다려야 할 수 도 있다.

위 방법으로 프린터가 작동할 때, 현재 대기 열에 있는 문서의 수와 우선순위가 주어졌을 때,
어떤 한 문서가 몇 번째 순서로 인쇄되는지 출력하는 프로그램을 작성하자.


첫 줄에 test case의 수가 주어진다.
각 test case에 대해서 문서의 수 N(<=100)와, 몇 번째로 인쇄 될지 궁금한 문서의 현재 대기 열 상 위치인 M(0 <= M < N)이 주어진다.
다음 줄에 N개 문서의 우선순위가 주어진다. ( 범위 : 1~9 ) 중요도가 같은 문서가 여러 개 있을 수도 있다.

입력 예시
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

-----------------------------------
각 test case에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

출력 예시
1
2
5
'''

import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline()
    N, M = map(int, readl().split())
    job = list(map(int, readl().split()))
    return N, M, job

def Solve(N, M, job):
    q = deque()
    cnt_prio = [0] * 10

    for idx, prio in enumerate(job):
        q.append((idx, prio))
        cnt_prio[prio] += 1

    cnt = 0 # 출력순서
    # for loop_prio

T = int(input())
sol = []

for _ in range(T):
    #입력받는 부분
    N, M, job = input_data()

    # 여기서부터 작성
    marks = ['x'] * N
    marks[M] = 'o'

    mark_q = deque()
    job_q = deque()

    mark_q += marks
    job_q += job

    print_order = 0
    while len(mark_q):
        biggest_job = find_max(job_q)
        m, j = mark_q.popleft(), job_q.popleft()
        if (j == biggest_job):
            print_order += 1
            if (m == 'o'):
                print(print_order)
                print_order = 0
                break
            else:
                continue
        else:
            mark_q.append(m)
            job_q.append(j)

    mark_q.clear() # deque
    job_q.clear()

    del mark_q     # deque
    del job_q

    del marks # o,x
