# 먼저 총을 list로 만듭니다
# (1) 터미네이터II는 임의의 사이즈를 가진 스택(탄창)을 생성(준비)할 수 있다.
myGun = []
print (myGun)

# 총에 총알(bullet)을 준비합니다
# (2) 터미네이터II는 데이터(=총알) 한 개를 추가(장전)할 수 있다.
myGun.append("bullet1")
myGun.append("bullet2")
myGun.append("bullet3")

print (myGun)


# 방아쇠를 당겨 발사합니다 빵~ 빵
# (3) 터미네이터II는 데이터(=총알) 한 개를 삭제(발사)할 수 있다.
print (myGun.pop())
print (myGun.pop())
print (myGun.pop())
print ("총알이 모두", len(myGun), "개 입니다")
# print (myGun)

print ("총알 발사!", myGun.pop())
# print ("top()", myGun.top()) # AttributeError: 'list' object has no attribute 'top'

weapon = {
    'pistol': ["bullet1", "bullet2", "bullet3", "bullet4", "bullet5", "bullet6"],
    'M1887': ["bullet1", "bullet2", "bullet3", "bullet4", "bullet5", "bullet6", "bullet7"]
}

import time
def fireGun(gun):
    while len(gun) > 0:
        print (gun.pop(), "발사~ 빵!")
        time.sleep(1)

fireGun (weapon['pistol'])