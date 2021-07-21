"""
1403 : 배열 두번 출력하기
https://codeup.kr/problem.php?id=1403
"""
N = int(input())

"""
map 은 iterator 가 동작하면, pointer 가 마지막을 가리키기 때문에
다시 map 객체를 초기화 하기 전까지는 두 번째 loop 을 돌 수 없다.
이에 map 을 list 로 변환 해 주도록 한다.
"""
number_list = list(map(int, input().split()))
"""
for _ in range(2):
    for v in number_list:
        print(v)
        """
for _ in range(2):
    [print(v) for v in number_list]