'''
<교재 page 220>

제시된 테스트 코드를 분석하여 In_Queue, Out_Queue함수를 완성하고 큐 함수를 검증하시오.
N개 만큼 입력 받은 정수가 양수이면 큐에 Write하고 0이면 Read하여 읽은 순서대로 출력한다.
만약 Read, Write동작에서 실패하면 -1을 출력한다.

[ 다음 함수들을 설계하라 ]
1] In_Queue함수의 기능은 다음과 같다.
 - prototype: int In_Queue(int d)
 - parameter: d는 큐에 저장할 값
 - 기능: d를 큐에 저장한다. 단, FULL 상태였다면 d를 큐에 저장하지 않고 Wp도 변경하지 않는다.
 - 리턴: 저장 성공하면 1을 리턴한다. 단, FULL 상태이면 반드시 0을 리턴 한다.

2] Out_Queue 함수의 기능은 다음과 같다.
 - prototype: int Out_Queue(void)
 - parameter: void
 - 기능: Read한 데이터를 리턴한다. 단, EMPTY이면 Rp의 내용은 변경하지 않는다.
 - 리턴: 읽기 성공하면 읽은 값을 리턴한다. 만약 EMPTY 상태면 Read 불가능 오류 코드로 0을 리턴 한다.

입력 설명
첫 줄에 정수 N을 입력 받아 둘째 줄에서 N개 만큼 정수를 입력 받는다. (1≤ N ≤20)

출력 설명
Read한 순서대로 출력한다.
만약 Read, Write동작에서 실패하면 -1을 출력한다.

입력 예시
11
1 2 3 4 0 0 0 5 0 0 0

출력 예시
1 2 3 4 5 -1
'''
import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	A = list(map(int, readl().split()))
	return N, A


def Push(d):
	global queue, wp, rp
	# 여기서부터 작성

def Pop():
	global queue, wp, rp
	# 여기서부터 작성

def Solve():
	for i in range(N):
		if A[i] > 0:
			r = Push(A[i])
			if r == 0: print(-1, end=' ')
		else:
			r = Pop()
			if r == 0: print(-1, end=' ')
			else: print(r, end=' ')


queue = [0]*5
wp = 0
rp = 0

# 입력받는 부분
N, A = Input_Data()

# 여기서부터 작성
Solve()