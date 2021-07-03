n = 6

primes = [False, False]
candidates = [True] * (n-2)

primes = primes + candidates

print(primes)

'''
for i in range(1, n+1):
    if (n % i == 0):
        print(i)
'''