# 각 로보트는
#  - 무기(weapon)를 소유하고 있습니다
#  - 차량(vehicle)을 타고 이동합니다
#  - 임무 수행용 복장을 하고 임무를 수행합니다

# 그런데, 아래 movie 코드에 문제는 각 로봇을 설명하는 데이터 상에 구분이 되어 있지 않은 것입니다
# 쉼표(comma)로 서로의 데이터를 구분합니다
# 아래와 같이 만들면 정상입니다
movie = {
    'T-1000': {
        "target": "존 코너",
        "weapon": "pistol",
        "vehicle": "sedan",
        "dress": "black police suite"
    },
    'terminator': {
        "target": "존 코너",
        "weapon": "M1887",
        "vehicle": "bike",
        "dress": "black leather jacket"
    }
}

weapon = {
    'pistol': ["bullet1", "bullet2", "bullet3", "bullet4", "bullet5", "bullet6"],
    'M1887': ["bullet1", "bullet2", "bullet3", "bullet4", "bullet5", "bullet6", "bullet7"]
}

print (movie['T-1000']['weapon'])
print (weapon['pistol'])
print (weapon['pistol'].pop()) #1발 발사합니다.
print (weapon['pistol'])

print ('--------5발 남은 상황에서 3발 쏘기----------')
print (weapon['pistol'].pop()) #1발 발사합니다.
print (weapon['pistol'].pop()) #1발 발사합니다.
print (weapon['pistol'].pop()) #1발 발사합니다.
print ('--------2발 남은 상황에서 4발 쏘기----------')
print (weapon['pistol'].pop()) #1발 발사합니다.
print (weapon['pistol'].pop()) #1발 발사합니다.
print (weapon['pistol'].pop()) #1발 발사합니다.
print (weapon['pistol'].pop()) #1발 발사합니다.




# 각 로봇의 주어진 임무
# mission 확인하기
# print ('T-1000',     "의 목표(target)는", movie['T-1000']['target'],    "(제거)입니다")
# print ('terminator', "의 목표(target)는", movie['terminator']['target'], "(보호)입니다")

# 존 코너를 사이에 두고 두 로보트가 서로 맞닥뜨렸습니다
# 각자의 mission이 실패하지 않으려면 weapon을 이용하여 상대를 저지해야 합니다.
# (발사!!) fire!!
print("콰앙~! ==> ", weapon[movie['T-1000']['weapon']].pop())

#
#
#
weapon[         'pistol'        ].pop()
weapon[                         ].pop()
weapon[movie['T-1000']['weapon']].pop()

#
weapon[           'M1887'           ].pop()
weapon[  movie['terminator']['weapon']   ].pop()

print (movie['terminator']['weapon'])








# terminator2heros = ["총알1", "banana", "cherry"]
#
# terminator2heros.append('haha')
# print(terminator2heros)
# terminator2heros.pop()
# print(terminator2heros)
#
# terminator2heros = ["apple", "banana", "cherry"]
# print(terminator2heros)
