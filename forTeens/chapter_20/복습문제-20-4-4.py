'''
중첩 반복 구조를 사용해서 다음과 같이 출력하는 파이썬 프로그램을 작성하세요
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
'''
for i in range(0, 6):
    for j in range(i+1):
        print(j, end=" ")
    print()