# https://codeup.kr/problem.php?id=1901

def print_number(num):
    if num <= 0:
        return
    print_number(num-1)
    print(num)

print_number(int(input()))