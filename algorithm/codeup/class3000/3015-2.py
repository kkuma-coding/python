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

# 입력되는 데이터를 받아오고, list 에 저장하는 과정
for i in range(people):
    name, score = input().split()
    score = int(score)
    scoreList.append((name, score))

# 정렬~
sortedScoreList = sorted(scoreList, key=lambda x: x[1], reverse=True)

#
for j in range(max):
    print(sortedScoreList[j][0])