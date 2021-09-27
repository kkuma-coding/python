val = int(input())
valStr = "{}".format(val)
size = len(valStr)

for i in range(0, size):
    print("[", end="")
    print (int(valStr[i])*(10**(size-i-1)), end="")
    print("]")