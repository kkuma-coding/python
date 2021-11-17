data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def bs(val):
    global data
    s, e = 0, len(data)-1
    m = 0
    while s <= e:
        m = (s + e) // 2
        if data[m] == val:
            return m
        elif data[m] < val:
            s = m + 1
        else:
            e = m - 1

    return -1 # not found


print("not found " if bs(33) == -1 else "found")
print("found" if bs(12) >= 0 else "not found")
print(bs(12))
print(bs(20))