def print_info():
    x = lambda x: x + 10
    return x(10)

def create_lambda(n):
    return lambda a : a * n

print(print_info())

d = create_lambda(2)
print (d(2), d(4), d(10))