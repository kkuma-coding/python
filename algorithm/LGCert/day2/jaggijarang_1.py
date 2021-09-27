# https://codepro.lge.com/exam/538/sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D-%EC%8B%A4%EC%A0%84-python-_210705/quiz/3
'''
JinYoung Cho - 조진영 님이 모두에게:    오전 9:18
  https://codepro.lge.com/go/assessment/JU5yJ6?sl=true
  여기로 들어가시면 됩니다
  이메일 / 이름 입력하시고..
'''
import sys

def input_data():
    readl = sys.stdin.readline
    N, S, M = map(int, readl().split())
    return N, S, M

sol_list = []

sabun = []

# 입력받는 부분
N, S, M = input_data()

# 여기서부터 작성
# sabun += [(s, j) for s, j in zip(list(range(1, N+1)), ['x']*7)]
sabun += list(range(1, N+1))
# print(sabun)
S = S -1
while len(sabun):
    idx = ((S)+(M-1)) % len(sabun)
    # print("시작", S, "거리", M - 1, "참조위치", idx)

    who = sabun.pop(idx)
    # print("-->", who, "번 발표")
    sol_list.append(who)

    S = idx

# 출력하는 부분
print(*sol_list)