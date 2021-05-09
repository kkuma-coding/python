'''
4 2
Jeon 95
Kim 59
Lee 90
Bae 100

{'Jeon': 95, 'Kim': 59, 'Lee': 90, 'Bae': 100}


4 1
Jeon 95
Kim 59
Lee 90
Bae 100
'''
people, max = input().split()
people, max = int(people), int(max)

scoreList = []

for i in range(people):
    name, score = input().split()
    score = int(score)
    scoreList.append([name, score])

sortedScoreList = sorted(scoreList, key=lambda x: x[1], reverse=True)
# print(sortedScoreList)
for j in range(max):
    print(sortedScoreList[j][0])