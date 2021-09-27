# https://codeup.kr/problem.php?id=1173
'''
수호는 30분 전으로 돌아가고 싶은 1人 이다.

공백을 기준으로 시간과 분이 주어진다.

그러면 이 시간을 기준으로 30분전의 시간을 출력하시오.

예)

12 35  =====> 12 5

12 0 ======> 11 30

11 5 ======> 10 35
'''
hh, mm = input().split()
hh, mm = int(hh), int(mm)
# hh, mm = 12, 35

subtract_hour = (30 > mm)
if subtract_hour is True:
    hh -= 1
    mm = 60 - (30 - mm)
else:
    mm -= 30

# if hh == 0:
#     hh = 12

if hh == -1:
    hh = 23

print (hh, mm)