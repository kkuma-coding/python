def maximum(val1, val2):
    m = val1
    if val2 > m:
        m = val2
    return m

#Main code starts here
a = float(input())
b = float(input())

maxim = maximum(a, b)

print(maxim)
