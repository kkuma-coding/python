'''
https://codeup.kr/problem.php?id=1160

주원이는 월, 수, 금, 일 아르바이트를 간다.

다음은 요일의 순서이다.

1. 월요일 *
2. 화요일
3. 수요일 *
4. 목요일
5. 금요일 *
6. 토요일
7. 일요일 *

요일의 번호가 입력으로 주어지면 그 날이 아르바이트 가는 날이면 "oh my god"를 가는 날이 아니면 "enjoy"를 출력하시오.
'''
day = int(input())
if (1<=day<=7 and day % 2 == 1):
    print ("oh my god")
else:
    print("enjoy")