from microbit import *

pos = 0
SIZE = 5
MAX = 25

def draw(pos):
    x = int(pos % SIZE)
    y = int (pos / SIZE)
    display.set_pixel (x, y, 5)

while True:
    for position in range(0, 25):
        draw(position)
        sleep(100)

    sleep(1000)
    display.clear()
