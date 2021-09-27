N = 8

start, end, grow = 0, N, N-1
print(start, end, "diff={}".format(end-start))

while(grow > 1):
    start, end, grow = end, end+grow, grow-1
    print(start, end, "diff={}".format(end-start))