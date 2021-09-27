"""
A = [list(map(int, "1 1 9 1 1 1 1".split())) for _ in range(7)]
print (A)
"""

job = map(int, "1 1 9 1 3 1 1".split())
for idx, prio in enumerate(job):
    print (idx, prio)