# http://www.codexpert.org/problem.php?cid=2104&dv=0&pid=1

'''
경상북도 특산품인 사과를 학생들에게 나눠주기 위해 여러 학교에 사과를 배정하였다.
배정된 사과 개수는 학교마다 다를 수 있고, 학생 수도 학교마다 다를 수 있다.
각 학교에서는 배정된 사과를 모든 학생들에게 똑같이 나눠주되, 남는 사과의 개수를 최소로 하려고 한다.
(서로 다른 학교에 속한 학생이 받는 사과 개수는 다를 수 있음)

예를 들어, 5개 학교의 학생 수와 배정된 사과 수가 다음과 같다고 하자.

각 학교의 학생 수와 사과 개수가 주어졌을 때,
학생들에게 나눠주고 남는 사과의 총 개수를 구하는 프로그램을 작성하시오.

<입력 값>
5
24 52
13 22
5 53
23 10
7 70

'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_data = [list(map(int,readl().split()))for _ in range(N)]
    S = [list_data[n][0] for n in range(N)]
    A = [list_data[n][1] for n in range(N)]
    return N, S, A


sol = -1
# 입력받는 부분
N, S, A = Input_Data()

# 여기서부터 작성
# print (type(N), S, A)

sum = 0
remain = 0
for i in range(len(S)):
    mok = A[i] // S[i]
    if (mok > 0):
        remain = A[i] - (S[i] * mok)
    else:
        remain = A[i]
    # print("Index", i, "사과", A[i], "학생", S[i], "남은양:", remain)
    sum += remain

# 출력하는 부분
print(sum)