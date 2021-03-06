size = 5

cell = dict()
celled = dict()

for i in range(0, size):
    for j in range(0, size):
        cell.update({tuple((i, j)): 0})

print (cell.keys())

print(cell)

print (cell.pop(   (0,0)     ))
