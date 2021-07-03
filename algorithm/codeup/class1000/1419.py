# https://codeup.kr/problem.php?id=1419
'''
영어 문장이 입력된다.
그 문장에서 love가 몇 번 나오는지 출력하시오.

소문자 love가 몇 번 나오는지 출력한다.
'''
count = 0

t = "love"
t_len = len(t)
value = "love lovely"
words = value.split()

test = "lovely"
for i in range(len(test)):
    for j in range(t_len):
        if (t[j] == test[i]):
            


'''
for w in words:
    if (t_len > len(w)):
        continue

    for i in range(len(w)):
        for j in range(t_len):
            if (w[i] == t[j]):

print(count)
'''