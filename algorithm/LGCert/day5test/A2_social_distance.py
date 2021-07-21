"""
문제 [5046] A2: [LAB] 사회적 거리두기
실행시간 제한: 1 Sec  메모리사용 제한: 128 MB
제출: 577  통과: 14.7%

농부 John은 전염성이 높은 COWVID-19이 발생한 이후, 소들의 건강이 걱정되었다.
병의 전염을 막기 위해서, 농부 John의 N마리 소들은 '사회적 거리두기' 실행하기로 결정하고 농장 전체에 흩어졌다. (2<=N<=105)
농부 John의 농장은 1차원 직선의 모양으로, M개의 서로 분리된 구간의 방목할 잔디가 구성되어 있다. (1<=M<=105)
소는 D의 값을 최대화하기 위해 각각 잔디구간의 정수 지점에 위치하려고 한다. 여기서 D는 가장 가까운 소 두 마리 사이의 거리를 말한다. 소가 D의 가능한 가장 큰 값을 가질수 있도록 도와주자.
(입력 예시에 대한 상황이 아래 '부가정보'에 그림으로 잘 표현되어 있다. 해당 내용을 참고하자.)

<<<입력 설명>>>
첫째 줄에는 N과 M이 주어진다. (2<=N<=105, 1<=M<=105)
다음 M개 줄에는 잔디구간을 나타내는 두개의 정수 a,b가 주어진다.(0<=a<b<=1018)
구간이 겹치거나 같은 지점에서 만나는 경우는 존재하지 않는다. 그리고 소들은 각 구간의 끝지점에도 서있을 수 있다.

<<<출력 설명>>>
가능 최대값 D를 출력하라. 모든 소들의 쌍은 D이상 떨어져 있어야 한다.
모든 입력은 0보다 큰 D값이 항상 존재한다.

<<<입력 예시>>>
5 3
0 2
4 7
9 9

<<<출력 예시>>>
2
"""
# coding=utf-8
import sys


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    intvals = [list(map(int, readl().split())) for _ in range(M)]
    return N, M, intvals


sol = -1
# 입력받는 부분
N, M, intvals = Input_Data()

intvals.sort()

s = intvals[0][0]
e = intvals[len(intvals)-1][1]
max_deploy = abs(e-s)+1

min_deploy_cow_cnt = N // M
rest_cows = N % M
# print(min_deploy_cow_cnt * N, rest_cows)

# 여기서부터 작성
# 값이 0일 수도 있을 것. 소가 0 마리라면.
# 한 구간에 최소 1마리는 들어갈 수 있다.
# 각각 잔디구간의 정수 지점에 위치하려고 한다. --> 건너 뛰는 구간 X
distance_list = []
for p1, p2 in intvals:
    dis = abs(p1-p2)
    # print("start:", p1, "end", p2, "간격:", dis, "최대 배치가능 소:", dis+1)
    distance_list.append(dis+1)


# print (s, e, max_deploy)

# 출력하는 부분
print(min_deploy_cow_cnt + min(distance_list))