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