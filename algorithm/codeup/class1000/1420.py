"""
https://codeup.kr/problem.php?id=1420

5
minsu 78
gunho 64
sumin 84
jiwon 96
woosung 55
"""
record = list()
count = int(input())
for x in range(count):
    name, score = input().split()
    score = int(score)
    record.append((score, name))

record.sort(key=lambda x:x[0], reverse=True)

print(record[2][1])