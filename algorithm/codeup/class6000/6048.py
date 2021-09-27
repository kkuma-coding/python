"""
1 9
True
"""
value = input()
a, b = value.split()
a = int(a)
b = int(b)

if (a < b):
    print(True)
else:
    print(False)