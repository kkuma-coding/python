# https://codeup.kr/problem.php?id=1901

def print_number(num):
    if num <= 0:
        return

    print(num)
    print_number(num-1)

print_number(int(input()))