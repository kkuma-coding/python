"""
https://www.geeksforgeeks.org/python-program-for-binary-search/
"""
A = [197, 101, 35, 97, 65, 161, 92, 100, 32, 95, 199,
     142, 176, 126, 167, 113, 189, 145, 77, 190, 193,
     194, 53, 190, 25, 3, 141, 8, 129, 82, 57, 27, 133,
     193, 153, 12, 2, 145, 87, 153, 84, 168, 189, 72,
     60, 134, 87, 76, 127, 28, 111, 131, 183, 136, 58,
     69, 81, 56, 62, 78, 179, 15, 134, 41, 57, 126, 112,
     24, 153, 90, 139, 84, 141, 182, 68, 31, 183, 7, 148,
     102, 29, 104, 35, 138, 15, 15, 119, 55, 133, 76, 29,
     132, 181, 191, 4, 40, 50, 141, 41, 133]


def bs(low, high, x):
    if high >= low:
        mid = (low + high) // 2

        if A[mid] == x:
            return mid
        elif A[mid] < x:
            return bs(mid+1, high, x)
        else:
            return bs(low, mid-1, x)
    else:
        return -1

A.sort()


low = 0
high = len(A)
print(bs(low, high, 4))
print(bs(low, high, 3))
print(bs(low, high, 153))