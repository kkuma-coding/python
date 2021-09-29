"""
https://opentutorials.org/course/4209/28516
"""

def f():
    global s
    s = "I love hyosun"
    print(s)

s = "I love ggamjee"
f()
print(s)