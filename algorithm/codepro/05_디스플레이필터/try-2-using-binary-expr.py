"""
이진 숫자를 만들어 내면, 조합 수를 만들어 낸 것과 동일하다는 idea 를 적용했다.
bin_format = "{:0" +str(N) + "b}"
for x in range(1, pow(2, N)-1): # MAX: 1024-1 : 11 1111 1111
    str_combi = bin_format.format(x)
    for i in range(N):
        if str_combi[i] == '0'

<input>
4
2 10
2 8
3 4
4 12

<output>
1

................................
<input>
5
1 183
2 40
4 5
6 3
8 1

<output>
2
"""
N = int(input())

R = []
P = []

for i in range(N):
    r, p = map(int, input().split())
    R.append(r)
    P.append(p)


candidate = []
min_diff = 987654321

candidate = []
bin_format = "{:0" +str(N) + "b}"
for x in range(1, pow(2, N)-1): # MAX: 1024-1 --> 11 1111 1111
    str_combi = bin_format.format(x)
    idx_list = [i for i in range(N) if str_combi[i] == '0']
    r_mul = 1
    p_sum = 0
    for i in idx_list:
        # idx = str_combi[i]
        r_mul *= R[i]
        p_sum += P[i]
    min_diff = min(min_diff, abs(r_mul-p_sum))
    candidate.append((min_diff, N-len(idx_list), str_combi))

candidate.sort(key=lambda x: (x[0], x[1]))

# print(candidate)

print(candidate[0][1])