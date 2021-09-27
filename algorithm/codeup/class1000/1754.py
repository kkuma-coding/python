"""
https://codeup.kr/problem.php?id=1754
9999999999999999999999999 9999999999999999999999998

266668686219689219623871546554333534783313444694818185252299570925151196408761294686484562969479593
5637945038352845600933001680168106341920289806616699139
"""
a, b = input().split()

if len(a) != len(b):
    if len(a) > len(b):
        print(b, a)
    else:
        print(a, b)
else:
    for i in range(len(a)):
        av = int(a[i])
        bv = int(b[i])
        if av == bv:
            continue
        elif av > bv:
            print (b, a)
            break
        else:
            print(a, b)
            break