"""
https://codeup.kr/problem.php?id=3212
6 8
1 2
2 3
2 4
3 4
3 6
4 5
4 6
5 6
"""
V, E = map(int, input().split())
fmap = []
[fmap.append([0]*(V+1)) for x in range(V+1)]
for _ in range(E):
    r, c = map(int, input().split())
    fmap[r][c] = 1

# before traverse
for row in fmap[1:]:
    print (*row[1:])

def dfs(r, c, path):
    if fmap[r][c] == 0:
        return []

    for i in len(fmap[c]):
        if fmap[c][i] == 1:
            candidate = path + dfs(c, i, path + [i])
            if len(candidate) == V:
                return candidate

    path + dfs(r, c, path)
    return path


for r in range(1, V+1):
    for c in range(1, V+1):
        dfscd ..