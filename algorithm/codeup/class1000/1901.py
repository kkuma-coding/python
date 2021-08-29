# https://codeup.kr/problem.php?id=1901

# 딱 바닥을 찍고 돌아오는 시점을 기준으로 생각하고 짜면 됨.
def print_number(num):
    if num <= 0:
        return

    print_number(num-1)
    print(num)

print_number(int(input()))