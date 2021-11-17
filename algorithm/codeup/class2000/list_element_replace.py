original = [1, 2, 0, 0, 0, 2, 1]
"""
for i in range(len(original)):
    if original[i] == 0:
        original[i] = 1
print(original)
"""

"""
<if/else 를 다 쓰는 경우.>
[f(x) if condition else g(x) for x in sequence]
<if 만 쓰는 경우>
[f(x) for x in sequence if condition]
"""
original[:] = [x if x != 0 else 1 for x in original]
print(original)

size = 7
fmap = []
for _ in range(size):
    fmap.append([0]*size)

fmap[3][:] = [1]*size
fmap[:][3] = [1]*size

for r in range(size):
    print(*fmap[r])