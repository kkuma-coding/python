"""
https://codeup.kr/problem.php?id=3019

순서없이 적힌 스케줄 메모가 있다.
메모는 스케줄명, 연, 월, 일 의 형태로 구성되어 있다.
이 메모를 토대로 날짜가 빠른 순서로 정렬하여 출력하고자 한다.
만약 날짜가 동일한 경우 스케줄명의 사전식 순서로 오름차순 정렬한다.

<입력>
5
sleep 2014 05 23
golf 2014 06 02
travel 2015 11 22
baseball 2013 02 01
study 2014 05 23

<출력>
baseball
sleep
study
golf
travel

<input>
입력:
20
sleepa 2014 05 23
golfb 2014 06 02
traveljp 2015 11 22
basketball 2013 02 01
studyabc 2014 05 23
sleepk 201 05 23
golf 2014 06 02
travelch 2014 11 22
baseballc 3 02 01
studybcc 2014 05 23
sleep 2014 05 23
golf 994 06 02
travel 15 11 22
baseballb 2013 02 01
study 2014 05 23
sleeph 2014 05 23
golfa 2014 05 02
travelusa 2015 11 23
basketball 2013 02 01
studyabc 2014 05 23

<output>
baseballc
travel
sleepk
golf
baseballb
basketball
basketball
golfa
sleep
sleepa
sleeph
study
studyabc
studyabc
studybcc
golf
golfb
travelch
traveljp
travelusa
"""

list_data = []

cnt = int(input())

for x in range(cnt):
    i_action, i_year, i_month, i_day = input().split()
    i_year = int(i_year)
    i_month = int(i_month)
    i_day = int(i_day)
    list_data.append((i_action, i_year, i_month, i_day))

list_data.sort(key=lambda x: (x[1], x[2], x[3], x[0]))

for t in list_data:
    print(t[0])