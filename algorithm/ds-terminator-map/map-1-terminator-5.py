robot = {
    1: {
        "name": "존 코너",
        "alias": "철 없지만 멋있는 미래의 주인공"
    },
    2: {
        "name": "사라 코너",
        "alias": "나는 엄마다. 나를 희생해도 자식은 보호한다"
    },
    3: {
        "name": "terminator",
        "alias": "터미네이터"
    },
    4: {
        "name": "T-1000",
        "alias": "액체인간. 무엇이든 복제할 수 있지. 목소리, 모습, 뭐든지 으하하"
    },
    15: {
        "name": "윤지호",
        "alias": "내 친구~~"
    }
}

# 여기 등장하는 모든 인물들의 이름을 알고 싶다.
for player in robot:
    print (robot[player]['alias'])
