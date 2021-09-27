'''
중첩 반복 구조를 사용해서 다음과 같은
삼각형을 출력하는 파이썬 프로그램을 작성하세요
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
starCount = 0
line = 9
for a in range(line):

    # a : 0, 1, 2, 3, 4(*****), 5, 6, 7, 8
    if(a<5):
        starCount = a+1
    else:
        starCount = line - a

    for b in range(starCount):
        print("*", end=" ")
    print()