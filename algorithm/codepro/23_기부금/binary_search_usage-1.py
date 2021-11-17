data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# let return index of
def bs(val):
    global data

    s, e = 0, len(data)-1

    while s<=e:
        m = (s + e) // 2
        if data[m] == val:
            return m
        elif data[m] < val:
            s = m + 1
        else:
            e = m - 1

    print(f"s={s}, e={e}, m={m}")

    return -1 # not found given value

print(bs(7))
print(bs(33))
