"""
https://codeup.kr/problem.php?id=3016

<<<입력>>>
첫째 줄에 데이터의 개수 n (3<=n<=100)
둘째 줄부터 n+1줄에 학생 이름과 3과목 점수들이 공백으로 구분되어 입력된다. (입력 예시 참고)
단 이름의 길이는 최대 10바이트 이내이다

<<<출력>>>
첫 번째 과목을 1등한 학생의 이름과 두 번째, 세 번째 과목의 석차를 공백으로 구분하여 출력한다.
단 첫 번째 과목의 1등은 1명이라고 가정한다.

<<<입력 예시>>>
4
Jeon 95 80 100
Kim 59 85 75
Lee 90 100 75
Bae 100 82 80

<<<출력 예시>>>
Bae 3 2

-----------------------------------------

<<<입력 예시>>>
4
Jeon 95 100 100
Kim 59 100 80
Lee 90 100 80
Bae 100 82 80

<<<출력 예시>>>
Bae 4 2
"""

N = int(input())
first_list = []
second_list = []
second_scores = []

third_list = []
third_scores = []

for idx in range(1, N+1):
    name, first, second, thrid = input().split()
    first = int(first)
    second = int(second)
    thrid = int(thrid)

    if not (second in second_scores):
        second_scores.append(second)
    if not (thrid in third_scores):
        third_scores.append(thrid)

    first_list.append( [first, idx, 0, name] )
    second_list.append( [second, idx, 0, name] )
    third_list.append( [thrid, idx, 0, name] )

second_scores.sort(reverse=True)
third_scores.sort(reverse=True)

first_list.sort(key=lambda x:x[0], reverse=True)
second_list.sort(key=lambda x:x[0], reverse=True)
third_list.sort(key=lambda x:x[0], reverse=True)

print(*second_scores)
print(*third_scores)

print(*first_list)
print(*second_list)
print(*third_list)

s_name = first_list[0][2]
print(s_name)
"""
idx_second = 0
for score, idx, n in second_list:
    if (n == s_name):
        break
    idx_second += 1
s_second_point = [idx_second]
idx_third = 1
for score, idx, n in third_list:
    if (n == s_name):
        break
    idx_third += 1

print(s_name, idx_second, idx_third)
"""
