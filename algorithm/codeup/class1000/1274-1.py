# https://codeup.kr/problem.php?id=1274
# complexity: O(N)
#
def isPrime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

# if (isPrime(int(input()))):
if (isPrime(4)):
    print("prime")
else:
    print("not prime")