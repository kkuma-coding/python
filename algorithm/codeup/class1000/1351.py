# https://codeup.kr/problem.php?id=1351
a, b = input().split()
a, b = int(a), int(b)

for value in range(a, b+1):
    for m in range(1,10):
        print ("{}*{}={}".format(value, m, value*m))