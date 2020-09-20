# 각 로보트는
#  - 무기(weapon)를 소유하고 있습니다
#  - 차량(vehicle)을 타고 이동합니다
#  - 임무 수행용 복장을 하고 임무를 수행합니다

# 그런데, 아래 movie 코드에 문제가 있습니다. 각자 코드를 고쳐주세요
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

# 각 로봇의 주어진 임무
# mission 확인하기
print ('T-1000', "의 목표(target)는", movie['T-1000']['target'], "(제거)입니다")
print ('terminator', "의 목표(target)는", movie['terminator']['target'], "(보호)입니다")

# 존 코너를 사이에 두고 두 로보트가 서로 맞닥뜨렸습니다
# 각자의 mission이 실패하지 않으려면 weapon을 이용하여 상대를 저지해야 합니다.
# (발사!!) fire!!
print("콰앙~! ==> ", weapon[movie['T-1000']['weapon']].pop())

print ("")

pass

weaponT1000 = ["bullet1", "bullet2", "bullet3", "bullet4", "bullet5", "bullet6"]
weaponTerminator = ["bullet1", "bullet2", "bullet3", "bullet4", "bullet5", "bullet6", "bullet7"]

terminator2heros = []
terminator2heros = ["총알1", "banana", "cherry"]

terminator2heros.append('haha')
print(terminator2heros)
terminator2heros.pop()
print(terminator2heros)

terminator2heros = ["apple", "banana", "cherry"]
print(terminator2heros)
