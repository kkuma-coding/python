# https://codeup.kr/problem.php?id=1064

# list = "10 3 7".split()
list = input().split()
out = []
for val in list:
    out.append(int(val))
out.sort()
print (out[0])