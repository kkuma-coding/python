from microbit import *

pos = 0
SIZE = 5
MAX = 25

def draw(pos):
    x = 4 - int(pos % SIZE)
    y = int (pos / SIZE)
    display.set_pixel (x, y, int(pos % SIZE)+1)

while True:
    for position in range (0, MAX):
        draw(position)
        sleep(100)
    sleep(1000)
    display.clear()