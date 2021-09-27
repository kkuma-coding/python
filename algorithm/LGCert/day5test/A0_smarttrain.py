"""
문제 [1209] A0: [LAB]지능형 기차
최근에 개발된 지능형 기차가 1번역(출발역)부터 4번역(종착역)까지
4개의 정차역이 있는 노선에서 운행되고 있다.

이 기차에는 타거나 내리는 사람 수를 자동으로 인식할 수 있는 장치가 있다.
이 장치를 이용하여 출발역에서 종착역까지 가는 도중 기차 안에 사람이 가장
많을 때의 사람 수를 계산하려고 한다.

단, 이 기차를 이용하는 사람들은 질서 의식이 투철하여,
역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 기차에 탄다고 가정한다.


각 역에서 내린 사람 수(0 이상, 10000 이하)와 탄 사람 수(0 이상, 10000 이하)가
빈칸을 사이에 두고 첫째 줄부터 넷째 줄까지 역 순서대로 한 줄에 하나씩 주어진다.

<<<input>>>
0 32
3 13
28 25
39 0

<<<output>>>
42

첫째 줄에 최대 사람 수를 출력한다.
"""
import sys

def Input_Data():
    readl = sys.stdin.readline
    list_inout = [list(map(int,readl().split())) for _ in range(4)]
    return list_inout


sol = -1
#입력받는 부분
list_inout = Input_Data()

#여기서 부터 작성
max = 0
q = []
q.append(-list_inout[0][0])
q.append(list_inout[0][1])
# print(q)
max = sum(q)
for p_out, p_in in list_inout[1:]:
    q.append(p_in)
    q.append(-p_out)
    s = sum(q)
    if (max < s):
        max = s

#출력 하는 부분
print(max)