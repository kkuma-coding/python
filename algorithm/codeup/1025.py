val = 75254
size = len("{:d}".format(val))

list = []
dividor = 10
for x in range(0, size-1):
    list.append(int(val / 10000) * 10000)
    val = val - list[len(list)-1]
    print (val)