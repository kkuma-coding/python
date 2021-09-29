a = 1
b = a
print("a =", a, " b =", b, ":", a is b)
print(id(a))
print(id(b))

b = 2
print("a =", a, " b =", b, ":", a is b)