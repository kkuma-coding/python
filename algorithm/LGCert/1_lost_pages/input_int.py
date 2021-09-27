"""
숫자를 두 개만 입력해야 한다.

<<<input>>
1 2

<<<output>>>
<class 'int'> <class 'int'>
"""
N, P = map(int, input().split())
print(type(N), type(P))

"""
<<<input>>>
1 2 3 4 5 6 7

<<<output>>>
"""
input_val_list = list(map(int, input().split()))
print(*input_val_list[:3])