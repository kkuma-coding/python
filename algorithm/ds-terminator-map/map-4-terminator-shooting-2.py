import time

print("프로그램을 시작하마마자 print() 실행됩니다.")
time.sleep(2.4)
print("2.4 초가 지난 뒤에 print() 실행됩니다.")

# 먼저 총을 list로 만듭니다
myGun = []

print (myGun.__class__)

# 총에 총알(bullet)을 준비합니다
myGun.append("bullet1")
myGun.append("bullet2")
myGun.append("bullet3")

print (myGun)

# 방아쇠를 당겨 발사합니다 빵~ 빵
print ("총알이 모두", len(myGun), "개 입니다")
print (myGun)

# prints out 1,2,3
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