'''
중첩 반복 구조를 사용해서 다음과 같이 출력하는 파이썬 프로그램을 작성하세요
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
# for idx in range(5, 0, -1):
#     print("{} ".format(idx) * idx)
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()