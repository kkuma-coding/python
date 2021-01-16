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
end = 9
dots = 0
for i in range(0, end):

    if i > 4:
        dots = end - i
    else:
        dots = i + 1

    for j in range(dots):
        print("* ", end=" ")
    print()