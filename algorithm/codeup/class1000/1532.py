# -2147483649
# -4294967296
def f():
    val = -1 << ((8*4)-1)
    return val - 1

print(f())